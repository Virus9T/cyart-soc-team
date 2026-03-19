# 🛡️ Week 2 – SOC Operations, Incident Response & Digital Forensics

This directory contains all **theoretical knowledge, practical assignments, workflow documentation** completed during Week 2 of SOC Lab training.

---

## 📂 Direct Access

- 📄 **Directly Access Reports (Screenshot attached):** [Open Reports Directory](./Reports)

---

## 📌 Overview

Week 2 focuses on building a strong foundation in **Security Operations Center (SOC)** processes including:

- Alert prioritization and classification  
- Incident response lifecycle  
- Threat triage and validation  
- Evidence collection and preservation  
- Full attack-to-response simulation (Capstone Project)  

---

## 📚 Theoretical Knowledge

### 1. Alert Priority Levels
- Classification: **Critical, High, Medium, Low**
- Based on:
  - Impact (data breach, service disruption)
  - Urgency (active exploitation)
- Risk scoring using **CVSS**
- Example:
  - CVSS 9.8 (Log4Shell) → Critical  

---

### 2. Incident Classification
- Incident Types:
  - Malware  
  - Phishing  
  - Brute-force  
  - Insider threats  
- Frameworks:
  - MITRE ATT&CK (e.g., T1566 – Phishing)
  - ENISA Taxonomy  
  - VERIS  
- Includes contextual metadata:
  - IP address  
  - Timestamps  
  - Indicators of Compromise (IOCs)  

---

### 3. Incident Response Lifecycle
Based on **NIST SP 800-61**:

1. Preparation  
2. Identification  
3. Containment  
4. Eradication  
5. Recovery  
6. Lessons Learned  

---

## ⚙️ Practical Applications

All practical assignments are denoted as:

**PA = Practical Application**
**The reports covering all the practical tasks are provided in the /Reports directory along with their respective screenshots**

---

### 📄 Completed Tasks

| Practical Application | Task | Description |
|----|------|------------|
| PA1 | Alert Management | Classification, prioritization, MITRE mapping |
| PA2 | Response Documentation | Incident reports, templates, checklists |
| PA3 | Alert Triage | Threat validation using Wazuh & threat intel |
| PA4 | Evidence Preservation | Memory dump, volatile data collection, hashing |
| PA5 | Capstone Project | Full attack → detection → response cycle |

---

## 🔄Workflow

### 1. Detection
- Alerts generated using **Wazuh**

### 2. Classification
- Assign severity:
  - Critical  
  - High  
  - Medium  
  - Low  
- Map alerts to **MITRE ATT&CK**

### 3. Triage
- Validate alerts using:
  - VirusTotal  
  - AlienVault OTX  

### 4. Investigation
- Analyze:
  - Logs  
  - Source IPs  
  - System activity  

### 5. Response
- Isolate affected system  
- Block malicious IP using:
  - CrowdSec  
  - Firewall  

### 6. Evidence Collection
- Collect volatile data using **Velociraptor**
  - Command: `netstat`  
- Acquire process memory dump:
  - `explorer.exe`  

### 7. Integrity Verification
- Generate SHA256 hash using **PowerShell**

### 8. Documentation
- Create incident reports  
- Maintain chain-of-custody  

---

## 🛠️ Tools Used

- **Wazuh** – SIEM for monitoring and alert generation  
- **Velociraptor** – Endpoint monitoring and memory acquisition  
- **PowerShell** – SHA256 hash generation  
- **VirusTotal / AlienVault OTX** – Threat intelligence validation  
- **Metasploit** – Attack simulation  
- **IPtables** – Threat mitigation and IP blocking  
- **Google Docs** – Documentation and reporting  
