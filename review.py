"""Beginner pattern-based checker for a few risky Python coding practices."""
import argparse
from pathlib import Path
import re

RULES = [
    ("HIGH", re.compile(r"\beval\s*\("), "Use of eval() can execute untrusted input.",
     "Avoid eval(); parse expected input with safer, explicit logic."),
    ("HIGH", re.compile(r"\bexec\s*\("), "Use of exec() can execute arbitrary code.",
     "Avoid exec() on dynamic or untrusted content."),
    ("HIGH", re.compile(r"\bpickle\.loads?\s*\("), "Pickle can execute code during deserialization.",
     "Do not load untrusted pickle data; use a safe data format such as JSON."),
    ("MEDIUM", re.compile(r"\bsubprocess\.(?:run|Popen|call)\s*\([^,\n]*\+"),
     "Possible shell/process command built with string concatenation.",
     "Pass a list of arguments and avoid shell=True; validate inputs."),
    ("MEDIUM", re.compile(r"\b(?:password|secret|api_key)\s*=\s*['\"][^'\"]+['\"]", re.I),
     "Possible hard-coded secret or credential.",
     "Use environment variables or a secrets manager; rotate exposed secrets."),
    ("LOW", re.compile(r"\bexcept\s*:\s*(?:pass)?\s*(?:#.*)?$"),
     "Bare exception handler may hide errors.",
     "Catch specific exceptions and log or handle them safely."),
]

def review(path: Path):
    try:
        lines = path.read_text(encoding="utf-8").splitlines()
    except (OSError, UnicodeError) as exc:
        print(f"Could not read file: {exc}")
        return 2

    findings = 0
    print(f"Secure Coding Review: {path}")
    print("=" * 60)
    for number, line in enumerate(lines, start=1):
        for severity, pattern, issue, fix in RULES:
            if pattern.search(line):
                findings += 1
                print(f"[{severity}] Line {number}: {issue}")
                print(f"  Remediation: {fix}")
    if not findings:
        print("No configured patterns detected.")
    print(f"\nSummary: {findings} finding(s).")
    print("Note: This educational pattern scanner can miss issues and report false positives.")
    return 0

def main():
    parser = argparse.ArgumentParser(description="Scan Python source for selected risky patterns.")
    parser.add_argument("file", type=Path, help="Python source file to review")
    args = parser.parse_args()
    raise SystemExit(review(args.file))

if __name__ == "__main__":
    main()
