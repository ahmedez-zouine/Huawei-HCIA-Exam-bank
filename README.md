# Huawei HCIA-Security V3.0 Master Exam Question Bank
### Comprehensive 1,050-Question Certification Preparation Guide & Conceptual Walkthrough

[![Certification](https://img.shields.io/badge/Huawei%20Certification-HCIA--Security%20V3.0-blue?style=for-the-badge&logo=huawei)](https://e.huawei.com/en/talent/#/cert/product-details?target=_blank&category=1&certId=14)
[![Exam Code](https://img.shields.io/badge/Exam%20Code-H12--711-red?style=for-the-badge)](https://e.huawei.com)
[![Total Questions](https://img.shields.io/badge/Question%20Bank-1%2C050%20Questions-green?style=for-the-badge)](data/full_question_bank.json)
[![LaTeX](https://img.shields.io/badge/Typeset%20with-LaTeX%20%2F%20TeX%20Live-brightgreen?style=for-the-badge&logo=latex)](main.tex)

A complete, publication-grade examination preparation system designed for engineers and students preparing for the **Huawei Certified ICT Associate in Security (HCIA-Security V3.0, Exam Code: H12-711)**.

---

## 📖 Overview

This repository contains an exhaustive question bank of **1,050 practice questions** systematically derived from the official 499-page Huawei HCIA-Security courseware. Every question is paired with a verified answer and a detailed conceptual explanation dissecting the underlying network security mechanisms.

### 🌟 Key Highlights

- **1,050 High-Yield Questions**:
  - **Part 1**: 420 Single-Choice Questions (Q1 – Q420)
  - **Part 2**: 320 Multiple-Choice Questions (Q421 – Q740)
  - **Part 3**: 310 True / False Questions (Q741 – Q1050)
- **Deep Conceptual Explanations**: Not just an answer key—each question features an accompanying green rationale card detailing *why* the correct answer is right, why distractors fail, and the underlying Huawei protocol logic.
- **Exhaustive 11-Chapter Curriculum Coverage**: 100% aligned with the official HCIA-Security V3.0 blueprint.
- **Quick Reference Master Answer Key**: Compact 5-column answer matrices at the end of the guide for rapid scoring.
- **Publication-Ready PDF**: Fully compiled 305-page PDF with custom `tcolorbox` cards, distinct category color themes, and clickable hyperlinks.

---

## 📊 Curriculum Syllabus & Question Distribution

| Ch. | Chapter Curriculum Topic | Single Choice (Pt 1) | Multi Choice (Pt 2) | True / False (Pt 3) | Chapter Total |
|:---:|:---|:---:|:---:|:---:|:---:|
| **1** | Network Security Concepts & Specifications | 36 | 26 | 26 | **88** |
| **2** | Network Basics (OSI, TCP/IP, Ethernet, IPv4/IPv6, Routing) | 44 | 34 | 32 | **110** |
| **3** | Common Network Security Threats & Defense | 36 | 28 | 26 | **90** |
| **4** | Firewall Overview & Stateful Inspection Principles | 40 | 30 | 30 | **100** |
| **5** | Firewall Security Policy & NAT Technologies | 42 | 32 | 30 | **104** |
| **6** | Dual-System Hot Standby & High Availability (VRRP, VGMP, HRP) | 38 | 30 | 28 | **96** |
| **7** | User Management & AAA Technology (RADIUS, HWTACACS, 802.1X) | 38 | 30 | 28 | **96** |
| **8** | Intrusion Prevention System (IPS, Signatures, Anti-DDoS) | 38 | 28 | 28 | **94** |
| **9** | Cryptography Foundations (DES, 3DES, AES, RSA, ECC, Hashes) | 34 | 26 | 25 | **85** |
| **10** | PKI Certificate System (ITU-T X.509, CA, RA, CRL, OCSP) | 34 | 26 | 25 | **85** |
| **11** | Encryption Technology Applications (IPsec AH/ESP, IKEv1/v2, L2TP, SSL VPN) | 40 | 30 | 32 | **102** |
| **--** | **Grand Totals Across Curriculum** | **420** | **320** | **310** | **1,050** |

---

## 🗂️ Repository Structure

```text
├── HCIA_Security_1050_Questions_Master_Guide.pdf  # Compiled 305-page PDF Book
├── main.tex                                       # Master LaTeX root document
├── preamble.tex                                   # Global LaTeX styling, colors & boxes
├── HCiA.pdf                                       # Official 499-page Courseware reference
│
├── chapters/                                      # Modular LaTeX chapter files
│   ├── exam_blueprint.tex                         # Syllabus blueprint & scoring guide
│   ├── part1_single_choice.tex                    # 420 Single Choice Questions
│   ├── part2_multi_choice.tex                     # 320 Multiple Choice Questions
│   ├── part3_true_false.tex                       # 310 True / False Questions
│   └── quick_answer_key.tex                       # Master Answer Key tables
│
├── data/                                          # Structured JSON exports
│   └── full_question_bank.json                    # All 1,050 questions with metadata
│
├── scripts/                                       # Python Question Generators
│   ├── build_full_database.py                     # Aggregator & LaTeX export pipeline
│   ├── generate_ch01_to_ch03.py                   # Chapter 1 generator
│   ├── generate_ch2.py to generate_ch11.py        # Chapters 2 through 11 generators
│
└── .gitignore                                     # Clean filter for LaTeX/Python artifacts
```

---

## 🛠️ Compilation & Usage

### 1. View the Compiled PDF Guide
You can directly open and read the compiled book:
- [`HCIA_Security_1050_Questions_Master_Guide.pdf`](HCIA_Security_1050_Questions_Master_Guide.pdf) (or `main.pdf`)

### 2. Re-compiling the LaTeX Document
To re-compile the book from source, ensure you have TeX Live / MacTeX installed with `pdflatex`:

```bash
# Run two passes to ensure TOC, cross-references, and bookmarks are synchronized
pdflatex -interaction=nonstopmode main.tex
pdflatex -interaction=nonstopmode main.tex
```

### 3. Re-generating the Question Database
If you edit or add questions inside the `scripts/generate_ch*.py` files, re-build the LaTeX chapters and JSON database using:

```bash
python3 scripts/build_full_database.py
```

---

## 🎨 Visual Design System

The document is typeset using a structured visual hierarchy:
- **Single Choice**: Teal accent border (`#0D9488`) with question cards and standard options.
- **Multiple Choice**: Royal purple accent border (`#6D28D9`) supporting multiple correct options.
- **True / False**: Amber accent border (`#D97706`) with binary selection.
- **Explanation Card**: Forest green header (`#047857`) and light green background (`#F0FDF4`) delivering clear technical rationales.

---

## 🎓 Exam Information

- **Exam Name**: Huawei Certified ICT Associate - Security
- **Exam Code**: H12-711
- **Format**: Single-Answer, Multiple-Answer, True/False
- **Duration**: 90 minutes
- **Passing Score**: 600 / 1000 points

---

## 📄 License & Disclaimer

This question bank was developed for educational and professional preparation purposes aligned with the Huawei Certified ICT Associate (HCIA) curriculum. All product names, logos, and trademarks are property of their respective owners.
