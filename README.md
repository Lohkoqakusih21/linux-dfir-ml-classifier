# linux-dfir-ml-classifier
🛠️ Linux Digital Forensics Automation with ML-Based File Classification

## 📌 Overview
This project presents a **Linux-based digital forensics automation framework** enhanced with **machine learning for intelligent file classification**.

Modern forensic investigations face a scalability challenge—large volumes of data, limited analysis time, and increasingly sophisticated threats. This system addresses that by automating triage and introducing **data-driven prioritization**.

Instead of manual inspection, files are treated as structured data and processed through an automated pipeline.

---

## 🎯 Objectives

- Automate large-scale forensic file analysis  
- Reduce manual triage effort  
- Detect suspicious and malicious artifacts beyond signature-based methods  
- Apply machine learning for intelligent classification  

---

## 🧠 Key Concept

> Malicious files often appear normal—but reveal anomalies when analyzed structurally.

This project leverages:
- **Entropy analysis** for detecting obfuscation  
- **Feature-based classification**  
- **Automated pipelines** for scalability  

---

## ⚙️ System Architecture


[Target Filesystem / Disk Image]
↓
[Data Acquisition]
↓
[Feature Extraction]
↓
[ML Classification]
↓
[Report Generation]


---

## 🚀 Features

- 📂 Recursive file scanning (Linux filesystem)
- 🔍 Feature extraction:
  - File size  
  - Shannon entropy  
- 🧠 Machine Learning classification:
  - Benign  
  - Suspicious  
  - Malicious  
- ⚙️ Automated processing pipeline  
- 📊 CSV-based reporting output  

---

## 🧬 Machine Learning Approach

- Model: **Random Forest Classifier**
- Input Features:
  - File size  
  - Entropy (randomness indicator)  
- Output:
  - File classification label  

This enables detection of:
- Packed malware  
- Encrypted payloads  
- Suspicious anomalies  
