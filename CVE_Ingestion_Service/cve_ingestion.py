import requests
import psycopg2

# DATABASE CONFIG

DB_HOST = "localhost"
DB_PORT = "5432"
DB_NAME = "vulndb"
DB_USER = "postgres"
DB_PASSWORD = "postgres"

# NVD API

NVD_URL = "https://services.nvd.nist.gov/rest/json/cves/2.0"

# EXTRACT METRICS

def extract_metrics(metrics):

    severity = "UNKNOWN"
    exploitability_score = None

    # Prefer newest CVSS version available
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
                "UNKNOWN"
            )

            break

    return severity, exploitability_score

# CONNECT DATABASE

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

# FETCH CVEs

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

print(f"[+] Received {len(vulnerabilities)} CVEs")

inserted = 0
skipped = 0

# PROCESS CVEs

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

    cur.execute(
        """
        INSERT INTO cves
        (
            cve_id,
            description,
            published_date,
            severity,
            exploitability_score
        )
        VALUES
        (
            %s,
            %s,
            %s,
            %s,
            %s
        )
        ON CONFLICT (cve_id)
        DO NOTHING
        """,
        (
            cve_id,
            description,
            published_date,
            severity,
            exploitability_score
        )
    )

    if cur.rowcount == 1:
        inserted += 1
    else:
        skipped += 1

# SAVE

conn.commit()

print()
print(f"[+] Inserted : {inserted}")
print(f"[+] Skipped  : {skipped}")

cur.close()
conn.close()

print("[+] Finished")