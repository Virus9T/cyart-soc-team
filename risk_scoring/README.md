# Python Based Risk Scoring system with CVE Ingestion service

A Python-based Risk Scoring System with CVE Ingestin service developed as part of the **CTEM Internship Project (Team 3 – Vulnerability & Risk Analysis)**.

The service retrieves vulnerability data from the **NIST National Vulnerability Database (NVD)**, extracts relevant security metrics, calculates a **Composite Risk Score**, and stores the processed data in a **PostgreSQL** database. It also supports a **local PostgreSQL fallback mechanism**, allowing risk scores to be recalculated even when the NVD API is unavailable.

---

# Features

- Fetches CVEs from the NVD CVE API
- Extracts:
  - CVE ID
  - Description
  - Published Date
  - Severity
  - Exploitability Score
- Calculates Composite Risk Score
- Stores processed CVEs in PostgreSQL
- Prevents duplicate CVEs using PostgreSQL UPSERT
- Local PostgreSQL cache fallback when NVD is unavailable (503)
- Displays sample processed CVEs in terminal

---

# Technologies Used

- Python 3.12+
- PostgreSQL
- psycopg2
- requests

---

# Requirements

## Python Packages

Install all required packages:


```bash
pip install -r requirements.txt
```

---

# PostgreSQL Requirements

Create a PostgreSQL database.

Example:

```
Database Name : vulndb
Username      : postgres
Password      : postgres
Port          : 5432
```

---

# Database Schema

Table Name

```
cves
```

Columns

| Column | Type |
|---------|------|
| id | SERIAL PRIMARY KEY |
| cve_id | VARCHAR(50) UNIQUE |
| description | TEXT |
| published_date | DATE |
| severity | VARCHAR(20) |
| exploitability_score | DOUBLE PRECISION |
| risk_score | DOUBLE PRECISION |

---

# Configure Database

Inside **risk_scoring_intigration.py**

```python
DB_HOST = "localhost"
DB_PORT = "5432"
DB_NAME = "vulndb"
DB_USER = "postgres"
DB_PASSWORD = "postgres"
```

Modify according to your PostgreSQL configuration.

---

# How the Program Works

```
NVD API
     │
     ▼
Download CVEs
     │
     ▼
Extract Metrics
     │
     ▼
Calculate Risk Score
     │
     ▼
Store into PostgreSQL
     │
     ▼
Display Sample Results
```

If the NVD API becomes unavailable:

```
NVD API
    │
    ▼
503 Error
    │
    ▼
Read Existing CVEs
from PostgreSQL
    │
    ▼
Recalculate Risk Scores
    │
    ▼
Update Database
```

---

# Risk Scoring Formula

The implemented risk score is based on the CTEM project specification.

```
Composite Risk Score =
(
Base Score
× Exploit Likelihood
× KEV Multiplier
× Asset Weight
× Exposure Multiplier
)
/
Normalization Factor
```

Where

```
Base Score = (CVSS × 10) + (Exploitability Score × 5)

Exploit Likelihood = EPSS × 100

KEV Multiplier

1.5 → Known Exploited Vulnerability

1.0 → Otherwise

Asset Weight

Low       = 1.0
Medium    = 1.5
High      = 2.0
Critical  = 3.0

Exposure

Restricted = 1.0
Internal   = 1.5
Internet   = 2.5
```

**Note:** EPSS, KEV status, Asset Criticality, and Exposure Context currently use placeholder values and can be replaced with real integrations in future versions.

---

# Running the Project

Start PostgreSQL.

Then execute

```bash
python risk_scoring_intigration.py
```

Example Output

```
[+] Connecting to PostgreSQL...
[+] Connected

[+] Downloading CVEs from NVD...

[+] Received 100 CVEs

[+] Inserted : 100
[+] Skipped  : 0

Sample CVEs

+----------------+----------+----------------+------------+
| CVE ID         | Severity | Exploitability | Risk Score |
+----------------+----------+----------------+------------+
| CVE-1999-0095  | HIGH     | 10.0           | 48.75      |
| CVE-1999-0082  | HIGH     | 10.0           | 48.75      |
+----------------+----------+----------------+------------+
```

---

# Duplicate Prevention

Duplicate CVEs are prevented using PostgreSQL UPSERT.

```sql
ON CONFLICT (cve_id)
DO UPDATE
```

This ensures

- Existing CVEs are updated
- New CVEs are inserted
- Duplicate records are avoided

---

# Local Cache Mechanism

If the NVD API is unavailable (503), the application automatically switches to the local PostgreSQL cache.

```
NVD API
     │
503 Error
     │
     ▼
Read Existing CVEs
     │
     ▼
Calculate Risk Scores
     │
     ▼
Update Database
```

This improves availability and reduces dependency on external services.

---

# Future Improvements

- Real EPSS API integration
- CISA KEV integration
- Asset Criticality API
- Exposure Context Integration
- REST API
- Flask Dashboard
- Risk Trend Visualization
- CVE Search API
- Scheduled Automatic Updates

---

# Author

**Tanay Sengupta**

Cybersecurity Intern

CTEM Internship Project

Team 3 – Vulnerability & Risk Analysis

---

# License

This project is intended for educational and internship demonstration purposes only.
