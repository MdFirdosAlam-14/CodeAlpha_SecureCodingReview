# Secure Coding Review

This project provides a small pattern-based Python checker and an intentionally insecure training sample.

## Run
From the project root:
```bash
python secure-coding-review/review.py secure-coding-review/examples/sample_app.py
```

## Sample findings
The example should demonstrate findings for hard-coded credentials and `eval()`. The checker also contains rules for unsafe pickle loading, possible command construction, and bare exception handlers.

## Limitations
This is a learning tool, not a complete SAST product. It uses regular expressions and can miss vulnerabilities or flag safe code. Confirm findings with manual review and established tools.
