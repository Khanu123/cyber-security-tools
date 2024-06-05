import unittest
from scripts.log_analysis.advanced_log_analyzer import analyze_log

class TestLogAnalyzer(unittest.TestCase):

    def test_analyze_log(self):
        log_data = """INFO: This is an info message
        WARNING: This is a warning message
        ERROR: This is an error message"""
        with open('test_log.txt', 'w') as f:
            f.write(log_data)

        expected_output = ["WARNING: This is a warning message", "ERROR: This is an error message"]

        with open('test_log.txt', 'r') as f:
            output = analyze_log(f, ["WARNING", "ERROR"])

        self.assertEqual(output, expected_output)

if __name__ == '__main__':
    unittest.main()
