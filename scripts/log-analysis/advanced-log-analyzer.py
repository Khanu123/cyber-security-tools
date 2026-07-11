import sys
import re


def compile_keywords(keywords):
    return [re.compile(keyword, re.IGNORECASE) for keyword in keywords]


def analyze_lines(lines, keywords):
    patterns = compile_keywords(keywords)
    findings = []
    for line in lines:
        if any(pattern.search(line) for pattern in patterns):
            findings.append(line.strip())
    return findings


def analyze_log(file_path, keywords):
    with open(file_path, "r", encoding="utf-8", errors="ignore") as file:
        return analyze_lines(file, keywords)


if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python advanced-log-analyzer.py <logfile> <keyword1> [<keyword2> ...]")
        sys.exit(1)

    log_file = sys.argv[1]
    keywords = sys.argv[2:]
    for finding in analyze_log(log_file, keywords):
        print(finding)
