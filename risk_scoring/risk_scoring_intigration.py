import requests
import psycopg2

# DATABASE CONFIG

DB_HOST = "localhost"
DB_PORT = "5432"
DB_NAME = "vulndb"
DB_USER = "postgres"
DB_PASSWORD = "postgres"

# NVD API

NVD_URL = "https://services.nvd.nist.gov/rest/json/cves/2.0?resultsPerPage=100"


# =====================================
# EXTRACT METRICS
# =====================================

def extract_metrics(metrics):

    severity = "UNKNOWN"
    exploitability_score = 0

    for metric_type in [
        "cvssMetricV31",
        "cvssMetricV30",
        "cvssMetricV2"
    ]:

        if metric_type in metrics:

            metric = metrics[metric_type][0]

            severity = metric.get(
                "baseSeverity",
                "UNKNOWN"
            )

            exploitability_score = metric.get(
                "exploitabilityScore",
                0
            )

            break

    return severity, exploitability_score


# =====================================
# RISK SCORING FORMULA
# =====================================

def calculate_risk_score(
    severity,
    exploitability_score
):

    # Dummy values for now #

    epss_score = 0.75
    kev_listed = False
    asset_criticality = "HIGH"
    exposure_context = "INTERNET"

    severity_to_cvss = {

        "CRITICAL": 9.5,
        "HIGH": 8.0,
        "MEDIUM": 5.5,
        "LOW": 3.0,
        "UNKNOWN": 1.0

    }

    cvss_score = severity_to_cvss.get(
        severity.upper(),
        1.0
    )
    try:
        exploitability_score = float(exploitability_score)
    except:
        exploitability_score = 0

    base_score = (
        (cvss_score * 10)
        +
        (float(exploitability_score) * 5)
    )

    exploit_likelihood = (
        epss_score * 100
    )

    kev_multiplier = (
        1.5 if kev_listed else 1.0
    )

    asset_weights = {
        "LOW": 1.0,
        "MEDIUM": 1.5,
        "HIGH": 2.0,
        "CRITICAL": 3.0
    }

    exposure_weights = {
        "RESTRICTED": 1.0,
        "INTERNAL": 1.5,
        "INTERNET": 2.5
    }

    asset_weight = asset_weights.get(
        asset_criticality,
        1.0
    )

    exposure_multiplier = exposure_weights.get(
        exposure_context,
        1.0
    )

    normalization_factor = 1000

    risk_score = (
        base_score
        * exploit_likelihood
        * kev_multiplier
        * asset_weight
        * exposure_multiplier
    ) / normalization_factor

    return round(
        risk_score,
        2
    )


# =====================================
# READ CVEs FROM DATABASE
# =====================================

def get_cves_from_database(cur):

    cur.execute(
        """
        SELECT
            cve_id,
            severity,
            exploitability_score
        FROM cves
        """
    )

    return cur.fetchall()


# =====================================
# CONNECT DATABASE
# =====================================

print("[+] Connecting to PostgreSQL...")

conn = psycopg2.connect(
    host=DB_HOST,
    port=DB_PORT,
    database=DB_NAME,
    user=DB_USER,
    password=DB_PASSWORD
)

cur = conn.cursor()

print("[+] Connected")


# =====================================
# FETCH CVEs
# =====================================

try:

    print("[+] Downloading CVEs from NVD...")

    response = requests.get(
        NVD_URL,
        timeout=60
    )

    response.raise_for_status()

    data = response.json()

    vulnerabilities = data.get(
        "vulnerabilities",
        []
    )

    print(
        f"[+] Received {len(vulnerabilities)} CVEs"
    )

    nvd_available = True

except Exception as e:

    print(
        f"[-] NVD unavailable: {e}"
    )

    print(
        "[+] Using CVEs from PostgreSQL cache..."
    )

    nvd_available = False


inserted = 0
skipped = 0


# =====================================
# FALLBACK TO DATABASE IF 500 ERROR
# =====================================

if not nvd_available:

    rows = get_cves_from_database(cur)

    updated = 0

    for row in rows:

        cve_id = row[0]
        severity = row[1]
        exploitability_score = row[2]

        risk_score = calculate_risk_score(
            severity,
            exploitability_score
        )

        cur.execute(
            """
            UPDATE cves
            SET risk_score = %s
            WHERE cve_id = %s
            """,
            (
                risk_score,
                cve_id
            )
        )

        updated += 1

    conn.commit()

    print(
        f"[+] Updated {updated} cached CVEs"
    )

    cur.close()
    conn.close()

    print("[+] Finished")

    exit()


# =====================================
# PROCESS CVEs
# =====================================

for vuln in vulnerabilities:

    cve = vuln["cve"]

    cve_id = cve.get("id")

    descriptions = cve.get(
        "descriptions",
        []
    )

    description = ""

    for item in descriptions:

        if item.get("lang") == "en":

            description = item.get(
                "value",
                ""
            )

            break

    published_date = cve.get(
        "published",
        ""
    )[:10]

    metrics = cve.get(
        "metrics",
        {}
    )

    severity, exploitability_score = (
        extract_metrics(metrics)
    )

    risk_score = calculate_risk_score(
        severity,
        exploitability_score
    )

    cur.execute(
        """
        INSERT INTO cves
        (
            cve_id,
            description,
            published_date,
            severity,
            exploitability_score,
            risk_score
        )
        VALUES
        (
            %s,
            %s,
            %s,
            %s,
            %s,
            %s
        )
        ON CONFLICT (cve_id)
        DO UPDATE
        SET

        severity =
        EXCLUDED.severity,

        exploitability_score =
        EXCLUDED.exploitability_score,

        risk_score =
        EXCLUDED.risk_score
        """,
        (
            cve_id,
            description,
            published_date,
            severity,
            exploitability_score,
            risk_score
        )
    )

    if cur.rowcount == 1:
        inserted += 1
    else:
        skipped += 1


# =====================================
# SAVE
# =====================================

conn.commit()

print()
print(f"[+] Inserted : {inserted}")
print(f"[+] Skipped  : {skipped}")

# =====================================
# DISPLAY SAMPLE CVEs FROM DATABASE
# =====================================

print("\n==============================================")
print(" CVEs Stored in PostgreSQL Database")
print("==============================================")

cur.execute(
    """
    SELECT
        cve_id,
        description,
        published_date,
        severity,
        exploitability_score,
        risk_score
    FROM cves
    ORDER BY id
    LIMIT 10;
    """
)

rows = cur.fetchall()

for row in rows:

    print("----------------------------------------------")
    print(f"CVE ID               : {row[0]}")
    print(f"Description          : {row[1]}")
    print(f"Published Date       : {row[2]}")
    print(f"Severity             : {row[3]}")
    print(f"Exploitability Score : {row[4]}")
    print(f"Risk Score           : {row[5]}")

print("----------------------------------------------")

cur.close()
conn.close()

print("[+] Finished")
