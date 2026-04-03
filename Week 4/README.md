# CYART SOC TEAM – WEEK 4

**Name:** Tanay Sengupta
**Role:** SOC Intern
**Organization:** CyArt Tech LLP
**Repository:** cyart-soc-team
**Week:** 4 Submission

---

## Objective

The objective of Week 4 was to strengthen advanced SOC analyst skills through threat hunting, alert triage automation, adversary emulation, incident response simulation, and SOC metrics reporting using industry-standard tools such as **Wazuh, Elastic Security, Velociraptor, MITRE Caldera, TheHive, CrowdSec, and Metasploit**.

---

## Tasks Completed

### 1. Threat Hunting Methodologies

Performed hypothesis-driven threat hunting using Elastic Security logs by analyzing privileged account activity (**Event ID 4672**). Findings were mapped with **MITRE ATT&CK technique T1078 (Valid Accounts)** and validated using threat intelligence sources like **AlienVault OTX** and **Velociraptor** queries.

---

### 2. SOAR Playbook Development

Designed an automated phishing-response workflow that checks IP reputation, blocks malicious IP addresses using **CrowdSec**, and creates incident cases in **TheHive**. This improved response efficiency and reduced manual investigation effort.

---

### 3. Post-Incident Analysis

Conducted Root Cause Analysis using the **5 Whys technique** on a simulated phishing scenario. The analysis identified weak filtering rules as the primary cause and highlighted the importance of improving detection configurations and threat intelligence integration.

---

### 4. Alert Triage with Automation

Analyzed a simulated suspicious file download alert in **Wazuh** and validated indicators using **VirusTotal** integration through **TheHive**. Automation helped speed up investigation and improved alert verification accuracy.

---

### 5. Evidence Analysis

Used **Velociraptor** to analyze endpoint network activity with system connection queries. Suspicious outbound connections were reviewed and documented while maintaining proper evidence handling practices and chain-of-custody awareness.

---

### 6. Adversary Emulation Practice

Simulated phishing attack behavior using **MITRE Caldera** mapped to **T1566 (Phishing)** and verified detection capability through **Wazuh** alerts. This helped evaluate SOC monitoring effectiveness against real-world attacker techniques.

---

### 7. Security Metrics and Reporting

Created a basic SOC metrics overview including **MTTD** and **MTTR** using **Elastic Security** dashboards. These metrics were used to evaluate detection speed and response performance.

---

### 8. Capstone Project – Incident Response Simulation

Simulated exploitation of a vulnerable service using **Metasploit** against a **Metasploitable2** environment mapped to **T1210 (Exploitation of Remote Services)**. The activity was detected in **Wazuh**, triaged in **TheHive**, and contained by blocking attacker IP using **CrowdSec**. Root cause analysis identified the vulnerability exposure as the primary issue.

---

## Conclusion

During Week 4, practical exposure was gained in:

* Threat hunting
* Automation workflows
* Adversary simulation
* Alert triage
* Evidence handling
* Incident response lifecycle management

These activities strengthened understanding of SOC monitoring operations aligned with **MITRE ATT&CK techniques** and real-world detection strategies.

