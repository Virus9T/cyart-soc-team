# 🛡️ Week 2 – SOC Operations, Incident Response & Digital Forensics

This directory contains all **theoretical knowledge, practical assignments, workflow documentation, and evidence artifacts** completed during Week 2 of SOC Lab training.

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

## ⚙️ Practical Assignments

All practical assignments are denoted as:

**PA = Practical Assignment**
**The reports covering all the practical tasks are provided in the /Reports directory along with their respective screenshots**

---

### 📄 Completed Tasks

| PA | Task | Description |
|----|------|------------|
| PA1 | Alert Management | Classification, prioritization, MITRE mapping |
| PA2 | Response Documentation | Incident reports, templates, checklists |
| PA3 | Alert Triage | Threat validation using Wazuh & threat intel |
| PA4 | Evidence Preservation | Memory dump, volatile data collection, hashing |
| PA5 | Capstone Project | Full attack → detection → response cycle |

---

## 🔄 SOC Workflow (Implemented)

```text
Alert Detection → Classification → Triage → Investigation → Response → Evidence Collection → Documentation
