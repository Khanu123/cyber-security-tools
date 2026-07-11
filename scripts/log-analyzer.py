import sys
import re


DEFAULT_PATTERN = re.compile(r"ERROR|CRITICAL|WARNING", re.IGNORECASE)


def analyze_lines(lines, pattern=DEFAULT_PATTERN):
    return [line.strip() for line in lines if pattern.search(line)]


def analyze_log(file_path):
    with open(file_path, "r", encoding="utf-8", errors="ignore") as file:
        return analyze_lines(file)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python log-analyzer.py <logfile>")
        sys.exit(1)

    log_file = sys.argv[1]
    for finding in analyze_log(log_file):
        print(finding)
