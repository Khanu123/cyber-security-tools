import sys
import re

def analyze_log(file_path, keywords):
    with open(file_path, 'r') as file:
        for line in file:
            for keyword in keywords:
                if re.search(keyword, line, re.IGNORECASE):
                    print(line.strip())

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python advanced-log-analyzer.py <logfile> <keyword1> [<keyword2> ...]")
        sys.exit(1)

    log_file = sys.argv[1]
    keywords = sys.argv[2:]
    analyze_log(log_file, keywords)
