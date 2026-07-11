# Cyber Security Tools

A collection of small Python security utilities for defensive learning, log analysis, network awareness, and authorized security testing.

## Overview

This repository is a learning lab for cybersecurity scripting. Each tool is intended to be simple enough to understand, but practical enough to demonstrate security concepts such as scanning, log review, and password-strength awareness.

## Included Tool Ideas

- `log-analyzer.py`: Review logs for suspicious keywords or repeated failures.
- `advanced-log-analyzer.py`: Enhanced log analysis with configurable indicators.
- `nmap-scan`: Authorized network scanning wrapper around Nmap.
- `hash-cracker.py`: Educational dictionary-based hash recovery lab.

## Skills Demonstrated

- Python automation
- Defensive log analysis
- Command-line tooling
- Security reporting
- Ethical boundaries for cybersecurity scripts

## Responsible Use

Only run scanning or password-recovery utilities in environments you own or have permission to test. This repo is for education, defensive practice, and authorized labs.

## Suggested Setup

```bash
git clone https://github.com/Khanu123/cyber-security-tools.git
cd cyber-security-tools
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```

If a specific tool has no external dependencies, it can be run directly with Python.

## Professional Roadmap

- Add one folder per tool with its own README.
- Add sample input and output for each script.
- Expand tests for parsing and detection functions.
- Add a top-level `docs/` folder with screenshots.
- Remove or clearly label any offensive examples as controlled lab exercises.

## Portfolio Note

For employers, this repository shows security curiosity and Python scripting practice. The strongest next step is to make each tool self-contained with examples and tests.

## Employer Review

| Area | Evidence |
| --- | --- |
| Role relevance | Junior Cyber Security Analyst / SOC Analyst / Python Automation |
| Main security lesson | Small scripts can support repeatable defensive checks when they are documented and scoped properly |
| Defensive value | Shows Python practice across logs, scanning wrappers, and controlled password-strength labs |
| Safe scope | Tools should only be used in owned or explicitly authorized environments |

## Professional Standards for This Repo

- Each script should have a clear purpose, expected input, and expected output.
- Any scanner should use conservative defaults and permission-based wording.
- Any password-related example should be framed as local password-strength education.
- Reports should be written in a way a junior analyst could hand to a teammate.
- Future tools should include tests before being treated as portfolio-ready.

## Interview Talking Points

- How Python helps automate repetitive security checks.
- Why defensive tools need clear authorization boundaries.
- How sample input/output makes a security script easier to review.
- Which scripts should be split into stronger standalone projects.

## Current Code Improvements

- Log analyzers now return findings as data as well as supporting CLI output.
- Advanced log analyzer has reusable keyword matching functions.
- Hash recovery lab supports selectable hash algorithms and returns results cleanly.
- Tests now work with the existing script filenames and folder layout.

## Testing

```bash
python -m unittest discover -s tests -v
```
