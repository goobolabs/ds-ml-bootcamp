#!/usr/bin/env python3
"""Scan submissions/ and generate SUBMISSIONS.md with assignment stats."""

from __future__ import annotations

import argparse
import re
from datetime import datetime, timezone
from pathlib import Path

WORD_TO_NUM = {
    "ten": 10,
    "nine": 9,
    "eight": 8,
    "seven": 7,
    "six": 6,
    "five": 5,
    "four": 4,
    "three": 3,
    "two": 2,
    "one": 1,
}


def compact_name(name: str) -> str:
    return re.sub(r"[\s_\-]+", "", name.lower())


def parse_assignment_number(folder_name: str) -> int | None:
    """Map a submission subfolder name to an assignment number, if possible."""
    compact = compact_name(folder_name)

    digit_match = re.search(r"(\d+)", compact)
    if digit_match:
        number = int(digit_match.group(1))
        if 1 <= number <= 99:
            return number

    for word, number in WORD_TO_NUM.items():
        if word in compact:
            return number

    return None


def scan_submissions(submissions_dir: Path) -> dict[str, set[int]]:
    """Return {student_name: {assignment_numbers}}."""
    students: dict[str, set[int]] = {}

    if not submissions_dir.is_dir():
        raise FileNotFoundError(f"Submissions directory not found: {submissions_dir}")

    for student_path in sorted(submissions_dir.iterdir()):
        if not student_path.is_dir():
            continue
        if student_path.name.lower() == "readme.md":
            continue

        assignments: set[int] = set()
        for child in student_path.iterdir():
            if not child.is_dir():
                continue
            number = parse_assignment_number(child.name)
            if number is not None:
                assignments.add(number)

        students[student_path.name] = assignments

    return students


def format_assignment_list(numbers: list[int]) -> str:
    if not numbers:
        return "none"
    return ", ".join(f"assignment {n}" for n in numbers)


def build_report(students: dict[str, set[int]]) -> str:
    all_assignments = sorted({n for nums in students.values() for n in nums})
    total = len(students)
    now = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")

    lines: list[str] = [
        "# Submission Stats",
        "",
        f"> Auto-generated report. Last updated: {now}",
        ">",
        "> A student counts as having submitted an assignment if a matching folder exists under their directory in `submissions/`.",
        "",
        f"**Total students:** {total}",
        "",
        "---",
        "",
        "## Summary",
        "",
    ]

    for number in all_assignments:
        sent = sum(1 for nums in students.values() if number in nums)
        not_sent = total - sent
        lines.append(
            f"- Assignment {number}: **{sent} sent**, **{not_sent} not sent** (out of {total})"
        )

    lines.extend(["", "---", "", "## Per-student breakdown", ""])

    for student in sorted(students, key=str.lower):
        submitted = sorted(students[student])
        missing = [n for n in all_assignments if n not in students[student]]

        if submitted:
            sent_text = f"sent {format_assignment_list(submitted)}"
        else:
            sent_text = "sent none"

        if missing:
            missing_text = f"did not send {format_assignment_list(missing)}"
        else:
            missing_text = "submitted all tracked assignments"

        lines.append(f"- **{student}** — {sent_text}; {missing_text}")

    lines.extend(["", "---", "", "## Students who did not send each assignment", ""])

    for number in all_assignments:
        missing_students = sorted(
            (s for s, nums in students.items() if number not in nums),
            key=str.lower,
        )
        lines.append(f"### Assignment {number} ({len(missing_students)} not sent)")
        lines.append("")
        if missing_students:
            for index, student in enumerate(missing_students, start=1):
                lines.append(f"{index}. {student}")
        else:
            lines.append("Everyone submitted this assignment.")
        lines.append("")

    return "\n".join(lines).rstrip() + "\n"


def main() -> None:
    parser = argparse.ArgumentParser(description="Generate submission stats report.")
    parser.add_argument(
        "--submissions-dir",
        type=Path,
        default=Path("submissions"),
        help="Path to submissions directory (default: submissions)",
    )
    parser.add_argument(
        "--output",
        type=Path,
        default=Path("SUBMISSIONS.md"),
        help="Output markdown file (default: SUBMISSIONS.md)",
    )
    args = parser.parse_args()

    repo_root = Path(__file__).resolve().parent.parent
    submissions_dir = args.submissions_dir
    if not submissions_dir.is_absolute():
        submissions_dir = repo_root / submissions_dir

    output_path = args.output
    if not output_path.is_absolute():
        output_path = repo_root / output_path

    students = scan_submissions(submissions_dir)
    report = build_report(students)
    output_path.write_text(report, encoding="utf-8")
    print(f"Wrote {output_path} ({len(students)} students)")


if __name__ == "__main__":
    main()
