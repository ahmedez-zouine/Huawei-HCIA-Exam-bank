# Huawei HCIA-Security V3.0 Master Exam Question Bank
### Comprehensive 1,050-Question Certification Preparation Guide & Conceptual Walkthrough

<p align="center">
  <img src="assets/cover_page_preview.png" alt="HCIA-Security Guide Cover" width="55%" style="border-radius: 6px; box-shadow: 0 4px 16px rgba(0,0,0,0.12);">
</p>

<p align="center">
  <a href="https://e.huawei.com/en/talent/#/cert/product-details?target=_blank&category=1&certId=14">
    <img src="https://img.shields.io/badge/Huawei%20Certification-HCIA--Security%20V3.0-1E3A8A?style=for-the-badge&logo=huawei" alt="Huawei Certification">
  </a>
  <img src="https://img.shields.io/badge/Exam%20Code-H12--711-DC2626?style=for-the-badge" alt="Exam Code">
  <a href="data/full_question_bank.json">
    <img src="https://img.shields.io/badge/Question%20Bank-1%2C050%20Questions-0D9488?style=for-the-badge" alt="Question Bank">
  </a>
  <a href="HCIA_Security_1050_Questions_Master_Guide.pdf">
    <img src="https://img.shields.io/badge/PDF%20Book-305%20Pages%20(1.5%20MB)-6D28D9?style=for-the-badge&logo=adobe-acrobat-reader" alt="PDF Book">
  </a>
  <img src="https://img.shields.io/badge/Typeset%20with-LaTeX%20%2F%20TikZ-047857?style=for-the-badge&logo=latex" alt="LaTeX">
</p>

---

A publication-grade examination preparation guide for engineers, security practitioners, and students preparing for the **Huawei Certified ICT Associate in Security (HCIA-Security V3.0, Exam Code: H12-711)** certification.

---

## 📑 Table of Contents
- [Key Highlights](#-key-highlights)
- [Curriculum & Question Distribution](#-curriculum-syllabus--question-distribution)
- [Sample Pages & Visual Design](#-sample-pages--visual-design)
- [Repository Structure](#-repository-structure)
- [Compilation & Build Guide](#-compilation--build-guide)
- [Exam Information & Strategy](#-exam-information--strategy)
- [License & Disclaimer](#-license--disclaimer)

---

## 🌟 Key Highlights

- **1,050 High-Yield Questions**:
  - **Part 1 (Single-Answer Questions)**: 420 Questions (Q1 – Q420)
  - **Part 2 (Multiple-Answer Questions)**: 320 Questions (Q421 – Q740)
  - **Part 3 (True / False Questions)**: 310 Questions (Q741 – Q1050)
- **Deep Conceptual Explanations**: Every single question is paired with an in-depth technical explanation box detailing *why* the correct answer is right, why other options are invalid, and the underlying Huawei protocol logic.
- **100% Official Curriculum Coverage**: Exhaustive coverage across all 11 modules of the official 499-page courseware (`HCiA.pdf`).
- **Master Quick-Reference Answer Key**: Compact 5-column answer matrices at the end of the book (Pages 300–305) for rapid mock exam scoring.
- **Pure LaTeX & TikZ Vector Design**: Clean, modern book typography with custom `tcolorbox` cards, distinct category color themes, and interactive PDF hyperlinks.

---

## 📊 Curriculum Syllabus & Question Distribution

| Ch. | Curriculum Module | Single Choice (Pt 1) | Multi Choice (Pt 2) | True / False (Pt 3) | Module Total |
|:---:|:---|:---:|:---:|:---:|:---:|
| **1** | **Network Security Concepts & Specifications**<br><sub>CIA triad, security standards, ISO/IEC 27001, China Classified Protection 2.0</sub> | 36 | 26 | 26 | **88** |
| **2** | **Network Basics**<br><sub>OSI 7-layer model, TCP/IP, Ethernet II frames, IPv4/IPv6 addressing, ICMP, ARP, routing basics</sub> | 44 | 34 | 32 | **110** |
| **3** | **Common Network Threats & Threat Prevention**<br><sub>Port scanning, SYN Flood, UDP/ICMP Flood, ARP spoofing, IP spoofing, malware, phishing</sub> | 36 | 28 | 26 | **90** |
| **4** | **Firewall Overview & Working Principles**<br><sub>Stateful inspection, security zones (Trust, Untrust, DMZ, Local), ASPF, session tables, server-map</sub> | 40 | 30 | 30 | **100** |
| **5** | **Firewall Security Policies & NAT Technologies**<br><sub>Security policy rules, 5-tuple matching, Easy IP, NAPT, NAT No-PAT, NAT Server, Smart NAT</sub> | 42 | 32 | 30 | **104** |
| **6** | **Dual-System Hot Standby & High Availability**<br><sub>VRRP protocol, VGMP management groups, HRP redundancy protocol, Active/Standby, Active/Active</sub> | 38 | 30 | 28 | **96** |
| **7** | **User Management & AAA Technologies**<br><sub>Authentication, Authorization, Accounting, RADIUS, HWTACACS, LDAP, AD, 802.1X, Portal, SACG</sub> | 38 | 30 | 28 | **96** |
| **8** | **Intrusion Prevention System (IPS)**<br><sub>Signature-based detection, behavioral analysis, false positive suppression, Anti-DDoS, traffic scrubbing</sub> | 38 | 28 | 28 | **94** |
| **9** | **Cryptography Foundations**<br><sub>Symmetric encryption (DES, 3DES, AES), Asymmetric encryption (RSA, ECC, DH), Hashes (MD5, SHA-1, SHA-2)</sub> | 34 | 26 | 25 | **85** |
| **10** | **PKI Certificate System & Applications**<br><sub>ITU-T X.509 certificates, CA, RA, CRL, OCSP, SCEP, digital signatures, certificate validation chains</sub> | 34 | 26 | 25 | **85** |
| **11** | **Encryption Technology Applications (IPsec & SSL VPN)**<br><sub>GRE over IPsec, AH (51), ESP (50), Transport/Tunnel modes, IKEv1 (Main/Aggressive/Quick), IKEv2, NAT-T, DPD, L2TP, SSL VPN (Web Proxy, File Sharing, Port Forwarding, Network Extension)</sub> | 40 | 30 | 32 | **102** |
| **--** | **Grand Totals Across Curriculum** | **420** | **320** | **310** | **1,050** |

---

## 📸 Sample Pages & Visual Design

### 1. Part 1: Single-Choice Questions (Teal Theme `#0D9488`)
Each question card features syllabus topic tags, standardized options, and an accompanying green explanation box.

<p align="center">
  <img src="assets/sample_single_choice.png" alt="Single Choice Sample Page" width="65%">
</p>

---

### 2. Part 2: Multiple-Choice Questions (Purple Theme `#6D28D9`)
Multiple-choice questions feature a royal purple theme with all correct options indicated in the explanation header and concepts dissected in depth.

<p align="center">
  <img src="assets/sample_multi_choice.png" alt="Multiple Choice Sample Page" width="65%">
</p>

---

### 3. Part 3: True / False Questions (Amber Theme `#D97706`)
True/False questions use an amber banner with explicit True/False verdicts and technical justifications.

<p align="center">
  <img src="assets/sample_true_false.png" alt="True/False Sample Page" width="65%">
</p>

---

### 4. Part 4: Master Quick-Reference Answer Key
High-density 5-pair table matrices (Pages 300–305) provide candidates with instant mock exam grading.

<p align="center">
  <img src="assets/sample_answer_key.png" alt="Answer Key Sample Page" width="65%">
</p>

---

## 🗂️ Repository Structure

```text
├── HCIA_Security_1050_Questions_Master_Guide.pdf  # Final Compiled 305-Page Master PDF Book
├── main.tex                                       # Main LaTeX root document
├── preamble.tex                                   # Layout, typography, colors, TikZ & tcolorbox
├── HCiA.pdf                                       # Official 499-page Courseware reference
│
├── assets/                                        # Visual Previews
│   ├── cover_page_preview.png                     # PDF cover page rendering
│   ├── sample_single_choice.png                   # Part 1 page preview
│   ├── sample_multi_choice.png                    # Part 2 page preview
│   ├── sample_true_false.png                      # Part 3 page preview
│   └── sample_answer_key.png                      # Part 4 answer key preview
│
├── chapters/                                      # Modular LaTeX Question Files
│   ├── exam_blueprint.tex                         # Syllabus blueprint & scoring guide
│   ├── part1_single_choice.tex                    # 420 Single Choice Questions (Q1 - Q420)
│   ├── part2_multi_choice.tex                     # 320 Multiple Choice Questions (Q421 - Q740)
│   ├── part3_true_false.tex                       # 310 True / False Questions (Q741 - Q1050)
│   └── quick_answer_key.tex                       # Quick Reference Master Answer Key
│
├── data/                                          # Structured JSON Datasets
│   └── full_question_bank.json                    # All 1,050 questions with complete metadata
│
├── scripts/                                       # Python Question Generators & Build Pipeline
│   ├── build_full_database.py                     # Aggregator & LaTeX export pipeline
│   ├── generate_ch01_to_ch03.py                   # Chapter 1 generator
│   └── generate_ch2.py ... generate_ch11.py       # Chapters 2 through 11 generators
│
└── .gitignore                                     # Clean filter for LaTeX/Python artifacts
```

---

## 🛠️ Compilation & Build Guide

### Direct Access
The compiled book is ready to read:
- **[`HCIA_Security_1050_Questions_Master_Guide.pdf`](HCIA_Security_1050_Questions_Master_Guide.pdf)** (305 pages, 1.5 MB)

### Recompiling with LaTeX
To re-compile the book from LaTeX source, ensure you have TeX Live / MacTeX installed:

```bash
# Run pdflatex twice to synchronize TOC, cross-references, and bookmarks
pdflatex -interaction=nonstopmode main.tex
pdflatex -interaction=nonstopmode main.tex

# Copy to release target
cp main.pdf HCIA_Security_1050_Questions_Master_Guide.pdf
```

### Rebuilding the Question Database
If you modify questions in any `scripts/generate_ch*.py` file, re-export the LaTeX chapters and JSON database:

```bash
python3 scripts/build_full_database.py
```

---

## 🎓 Exam Information & Strategy

| Parameter | Specification |
|:---|:---|
| **Certification Name** | Huawei Certified ICT Associate - Security |
| **Exam Code** | **H12-711** |
| **Exam Format** | Single Choice, Multiple Choice, True / False |
| **Question Count** | ~60 questions (in live exam) |
| **Exam Duration** | 90 Minutes |
| **Total Score** | 1,000 Points |
| **Passing Score** | **600 Points** (60%) |
| **Recommended Strategy** | Work through each chapter sequentially. Self-assess using the Master Answer Key (Pages 300–305), and read the Explanation Box for any missed questions to solidify core concepts. |

---

## 📄 License & Disclaimer

This preparation bank was authored for educational, training, and certification preparation purposes aligned with the Huawei Certified ICT Associate (HCIA) curriculum. All Huawei product names, logos, trademarks, and registered trademarks (`USG`, `SecoPath`, `HRP`, `VGMP`) are property of Huawei Technologies Co., Ltd.
