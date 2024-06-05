import sys
import re

def analyze_log(file_path):
    with open(file_path, 'r') as file:
        for line in file:
            if re.search(r"ERROR|CRITICAL|WARNING", line):
                print(line.strip())

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python log-analyzer.py <logfile>")
        sys.exit(1)

    log_file = sys.argv[1]
    analyze_log(log_file)
