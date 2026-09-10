# scripts/build_full_database.py
"""
Builds the complete dataset of 1,050 questions for HCIA-Security V3.0
- Part 1: 420 Single Choice questions (Q1 to Q420)
- Part 2: 320 Multiple Choice questions (Q421 to Q740)
- Part 3: 310 True/False questions (Q741 to Q1050)
Total = 1,050 questions.

Exports:
- data/full_question_bank.json
- chapters/exam_blueprint.tex
- chapters/part1_single_choice.tex
- chapters/part2_multi_choice.tex
- chapters/part3_true_false.tex
- chapters/quick_answer_key.tex
"""
import os
import sys
import json
import re

# Ensure scripts dir is in path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from generate_ch01_to_ch03 import build_ch1
from generate_ch2 import get_ch2_questions
from generate_ch3 import get_ch3_questions
from generate_ch4 import get_ch4_questions
from generate_ch5 import get_ch5_questions
from generate_ch6 import get_ch6_questions
from generate_ch7 import get_ch7_questions
from generate_ch8 import get_ch8_questions
from generate_ch9 import get_ch9_questions
from generate_ch10 import get_ch10_questions
from generate_ch11 import get_ch11_questions

CHAPTER_METADATA = [
    (1, "Network Security Concepts and Specifications", build_ch1),
    (2, "Network Basics", get_ch2_questions),
    (3, "Common Network Security Threats and Threat Prevention", get_ch3_questions),
    (4, "Firewall Overview and Working Principles", get_ch4_questions),
    (5, "Firewall Security Policy and NAT Technology", get_ch5_questions),
    (6, "Firewall High Availability (VRRP & VGMP)", get_ch6_questions),
    (7, "User Management and AAA Technology", get_ch7_questions),
    (8, "Intrusion Prevention System (IPS) and Defense", get_ch8_questions),
    (9, "Cryptography Foundations and Encryption Technology", get_ch9_questions),
    (10, "PKI Certificate System and Applications", get_ch10_questions),
    (11, "Encryption Technology Applications (IPsec & SSL VPN)", get_ch11_questions),
]

def escape_latex(s):
    if not isinstance(s, str):
        return str(s)
    # Handle backticks: `code` -> \texttt{code}
    parts = re.split(r'(`[^`]+`)', s)
    out = []
    for part in parts:
        if part.startswith('`') and part.endswith('`'):
            inner = part[1:-1]
            inner = inner.replace('\\', r'\textbackslash{}')
            for char in ['&', '%', '$', '#', '_', '{', '}']:
                inner = inner.replace(char, '\\' + char)
            inner = inner.replace('~', r'\textasciitilde{}')
            inner = inner.replace('^', r'\textasciicircum{}')
            inner = inner.replace('<', r'\textless{}')
            inner = inner.replace('>', r'\textgreater{}')
            out.append(r'\texttt{' + inner + '}')
        else:
            txt = part.replace('\\', r'\textbackslash{}')
            for char in ['&', '%', '$', '#', '_', '{', '}']:
                txt = txt.replace(char, '\\' + char)
            txt = txt.replace('~', r'\textasciitilde{}')
            txt = txt.replace('^', r'\textasciicircum{}')
            txt = txt.replace('<', r'\textless{}')
            txt = txt.replace('>', r'\textgreater{}')
            # Typographic double quotes
            txt = re.sub(r'(^|[\s\(\[\{])"([^\"]+)"', r"\1``\2''", txt)
            out.append(txt)
    return ''.join(out)

def build_all_questions():
    all_single = []
    all_multi = []
    all_tf = []
    ch_stats = []

    for ch_num, ch_title, gen_func in CHAPTER_METADATA:
        s_list, m_list, t_list = gen_func()
        ch_stats.append({
            "num": ch_num,
            "title": ch_title,
            "single": len(s_list),
            "multi": len(m_list),
            "tf": len(t_list),
            "total": len(s_list) + len(m_list) + len(t_list)
        })
        all_single.extend(s_list)
        all_multi.extend(m_list)
        all_tf.extend(t_list)

    # Assign Sequential QIDs
    # Part 1: Q1 to Q420
    for idx, q in enumerate(all_single, start=1):
        q["qid"] = idx
        q["part"] = 1

    # Part 2: Q421 to Q740
    for idx, q in enumerate(all_multi, start=421):
        q["qid"] = idx
        q["part"] = 2

    # Part 3: Q741 to Q1050
    for idx, q in enumerate(all_tf, start=741):
        q["qid"] = idx
        q["part"] = 3

    return all_single, all_multi, all_tf, ch_stats

def write_exam_blueprint(ch_stats, out_path):
    lines = [
        r"\section*{HCIA-Security V3.0 Exam Blueprint \& Question Distribution}",
        r"\addcontentsline{toc}{section}{HCIA-Security V3.0 Exam Blueprint \& Question Distribution}",
        r"",
        r"The Huawei Certified ICT Associate in Security (\textbf{HCIA-Security V3.0}, Exam Code: \textbf{H12-711}) validates that engineers possess foundational knowledge of enterprise network security architectures, Huawei firewall technologies, AAA user authentication, intrusion prevention, cryptographic principles, and VPN deployment. The examination consists of Single-Choice, Multiple-Choice, and True/False questions with a passing threshold of 600 out of 1000 points.",
        r"",
        r"\vspace{0.8em}",
        r"\noindent This comprehensive question bank comprises \textbf{1,050 fully annotated questions} systematically organized into three distinct parts, spanning all 11 curriculum modules:",
        r"",
        r"\begin{table}[h!]",
        r"\centering",
        r"\small",
        r"\begin{tabular}{clcccc}",
        r"\toprule",
        r"\textbf{Ch.} & \textbf{Chapter Curriculum Topic} & \textbf{Single (Pt 1)} & \textbf{Multi (Pt 2)} & \textbf{T/F (Pt 3)} & \textbf{Total Questions} \\",
        r"\midrule"
    ]
    tot_s, tot_m, tot_t, tot_all = 0, 0, 0, 0
    for s in ch_stats:
        lines.append(f"{s['num']} & {escape_latex(s['title'])} & {s['single']} & {s['multi']} & {s['tf']} & {s['total']} \\\\")
        tot_s += s['single']
        tot_m += s['multi']
        tot_t += s['tf']
        tot_all += s['total']
    lines.extend([
        r"\midrule",
        f"\\textbf{{--}} & \\textbf{{Total Questions Across Curriculum}} & \\textbf{{{tot_s}}} & \\textbf{{{tot_m}}} & \\textbf{{{tot_t}}} & \\textbf{{{tot_all}}} \\\\",
        r"\bottomrule",
        r"\end{tabular}",
        r"\end{table}",
        r"",
        r"\vspace{0.8em}",
        r"\noindent\textbf{Structure of Each Question Entry:}",
        r"\begin{itemize}[leftmargin=1.8em, itemsep=2pt]",
        r"    \item \textbf{Question Card:} Features the unique question number (QID), category accent color, specific syllabus topic tag, question stem, and standardized options (A, B, C, D).",
        r"    \item \textbf{Explanation Box:} Immediately follows each question card with the verified correct answer in the header, followed by an in-depth conceptual explanation elucidating \textit{why} the correct option is right, why distractors are incorrect, and the core Huawei HCIA-Security principle at work.",
        r"    \item \textbf{Quick Answer Key:} Appendix at the end of the volume featuring compact reference matrices for rapid self-assessment and mock exam scoring.",
        r"\end{itemize}",
        r"\clearpage",
        r""
    ])
    with open(out_path, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))
    print(f"Written: {out_path}")

def format_question_latex(q, accent_col):
    qid = q["qid"]
    topic = escape_latex(q.get("topic", ""))
    qtype = escape_latex(q.get("type", ""))
    stem = escape_latex(q.get("stem", ""))
    options = q.get("options", [])
    answer = q.get("answer", "")
    explanation = escape_latex(q.get("explanation", ""))

    lines = []
    lines.append(f"\\begin{{qcard}}{{{qid}}}{{{accent_col}}}")
    lines.append(f"\\textcolor{{darkslate!75}}{{\\small\\textbf{{Topic:}} {topic} \\hfill \\textbf{{Type:}} {qtype}}}\\vspace{{0.4em}}\\par")
    lines.append(stem)
    lines.append(r"\begin{qoptions}")
    for opt in options:
        lines.append(f"\\item {escape_latex(opt)}")
    lines.append(r"\end{qoptions}")
    lines.append(r"\end{qcard}")
    lines.append(r"\nopagebreak")

    # Explanation box header formatting
    if qtype == "True/False":
        ans_display = f"{answer} (True)" if answer == "A" else f"{answer} (False)"
    elif qtype == "Multiple Choice":
        ans_display = ", ".join(list(answer))
    else:
        ans_display = answer

    lines.append(f"\\begin{{explainbox}}{{{ans_display}}}")
    lines.append(f"\\textbf{{Concept \\& Rationale:}} {explanation}")
    lines.append(r"\end{explainbox}")
    lines.append("")
    return "\n".join(lines)

def write_part_file(questions, filename, accent_col, part_title):
    grouped = {}
    for q in questions:
        ch = q["chapter_num"]
        if ch not in grouped:
            grouped[ch] = []
        grouped[ch].append(q)

    lines = []
    for ch_num in sorted(grouped.keys()):
        ch_title = grouped[ch_num][0]["chapter_title"]
        lines.append(f"\\section{{Chapter {ch_num}: {escape_latex(ch_title)}}}")
        lines.append("")
        for q in grouped[ch_num]:
            lines.append(format_question_latex(q, accent_col))

    with open(filename, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))
    print(f"Written: {filename} ({len(questions)} questions)")

def write_quick_answer_key(all_single, all_multi, all_tf, out_path):
    lines = [
        r"\section*{Quick Reference Answer Key}",
        r"\addcontentsline{toc}{section}{Quick Reference Answer Key}",
        r"",
        r"Use these quick-reference matrices to rapidly cross-check your mock exam responses.",
        r"",
        r"\subsection*{Part 1: Single Choice Answers (Q1 -- Q420)}",
        r"\small",
        r"\begin{longtable}{cc|cc|cc|cc|cc}",
        r"\toprule",
        r"\textbf{Q\#} & \textbf{Ans} & \textbf{Q\#} & \textbf{Ans} & \textbf{Q\#} & \textbf{Ans} & \textbf{Q\#} & \textbf{Ans} & \textbf{Q\#} & \textbf{Ans} \\",
        r"\midrule",
        r"\endhead"
    ]

    # Format Single Choice: 5 per row
    for i in range(0, len(all_single), 5):
        chunk = all_single[i:i+5]
        row_items = []
        for q in chunk:
            row_items.append(f"{q['qid']} & {q['answer']}")
        while len(row_items) < 5:
            row_items.append("&")
        lines.append(" & ".join(row_items) + r" \\")

    lines.extend([
        r"\bottomrule",
        r"\end{longtable}",
        r"",
        r"\clearpage",
        r"\subsection*{Part 2: Multiple Choice Answers (Q421 -- Q740)}",
        r"\small",
        r"\begin{longtable}{cc|cc|cc|cc|cc}",
        r"\toprule",
        r"\textbf{Q\#} & \textbf{Ans} & \textbf{Q\#} & \textbf{Ans} & \textbf{Q\#} & \textbf{Ans} & \textbf{Q\#} & \textbf{Ans} & \textbf{Q\#} & \textbf{Ans} \\",
        r"\midrule",
        r"\endhead"
    ])

    # Format Multiple Choice: 5 per row
    for i in range(0, len(all_multi), 5):
        chunk = all_multi[i:i+5]
        row_items = []
        for q in chunk:
            row_items.append(f"{q['qid']} & {q['answer']}")
        while len(row_items) < 5:
            row_items.append("&")
        lines.append(" & ".join(row_items) + r" \\")

    lines.extend([
        r"\bottomrule",
        r"\end{longtable}",
        r"",
        r"\clearpage",
        r"\subsection*{Part 3: True / False Answers (Q741 -- Q1050)}",
        r"\small",
        r"\begin{longtable}{cc|cc|cc|cc|cc}",
        r"\toprule",
        r"\textbf{Q\#} & \textbf{Ans} & \textbf{Q\#} & \textbf{Ans} & \textbf{Q\#} & \textbf{Ans} & \textbf{Q\#} & \textbf{Ans} & \textbf{Q\#} & \textbf{Ans} \\",
        r"\midrule",
        r"\endhead"
    ])

    # Format True/False: 5 per row, show T or F
    for i in range(0, len(all_tf), 5):
        chunk = all_tf[i:i+5]
        row_items = []
        for q in chunk:
            tf_str = "True" if q['answer'] == "A" else "False"
            row_items.append(f"{q['qid']} & {tf_str}")
        while len(row_items) < 5:
            row_items.append("&")
        lines.append(" & ".join(row_items) + r" \\")

    lines.extend([
        r"\bottomrule",
        r"\end{longtable}",
        r""
    ])

    with open(out_path, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))
    print(f"Written: {out_path}")

def main():
    print("=== Building Full HCIA-Security Question Database (1,050 Questions) ===")
    os.makedirs("chapters", exist_ok=True)
    os.makedirs("data", exist_ok=True)

    all_single, all_multi, all_tf, ch_stats = build_all_questions()

    total_q = len(all_single) + len(all_multi) + len(all_tf)
    print(f"Aggregated Questions: {len(all_single)} Single, {len(all_multi)} Multi, {len(all_tf)} TF. Total = {total_q}")

    # Export complete JSON database
    full_db = {
        "metadata": {
            "title": "HCIA-Security V3.0 Complete Exam Question Bank",
            "exam_code": "H12-711",
            "total_questions": total_q,
            "single_choice_count": len(all_single),
            "multi_choice_count": len(all_multi),
            "true_false_count": len(all_tf),
            "chapter_distribution": ch_stats
        },
        "questions": all_single + all_multi + all_tf
    }

    json_path = os.path.join("data", "full_question_bank.json")
    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(full_db, f, indent=2, ensure_ascii=False)
    print(f"Exported JSON database: {json_path}")

    # Write TeX chapters
    write_exam_blueprint(ch_stats, os.path.join("chapters", "exam_blueprint.tex"))
    write_part_file(all_single, os.path.join("chapters", "part1_single_choice.tex"), "singlecol", "Single-Answer Questions")
    write_part_file(all_multi, os.path.join("chapters", "part2_multi_choice.tex"), "multicol", "Multiple-Answer Questions")
    write_part_file(all_tf, os.path.join("chapters", "part3_true_false.tex"), "tfcol", "True / False Questions")
    write_quick_answer_key(all_single, all_multi, all_tf, os.path.join("chapters", "quick_answer_key.tex"))

    print("=== All Question Bank Modules Successfully Generated ===")

if __name__ == "__main__":
    main()
