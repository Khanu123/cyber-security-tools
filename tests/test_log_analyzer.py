import importlib.util
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def load_module(path, name):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class TestLogAnalyzer(unittest.TestCase):
    def test_basic_analyzer_returns_matching_lines(self):
        module = load_module(ROOT / "scripts" / "log-analyzer.py", "log_analyzer")
        lines = ["INFO ok", "WARNING risky", "ERROR failed"]
        self.assertEqual(module.analyze_lines(lines), ["WARNING risky", "ERROR failed"])

    def test_advanced_analyzer_returns_keyword_matches(self):
        module = load_module(
            ROOT / "scripts" / "log-analysis" / "advanced-log-analyzer.py",
            "advanced_log_analyzer",
        )
        lines = ["INFO ok", "failed login", "admin success"]
        self.assertEqual(module.analyze_lines(lines, ["failed"]), ["failed login"])


if __name__ == "__main__":
    unittest.main()
