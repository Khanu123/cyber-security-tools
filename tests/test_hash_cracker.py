import importlib.util
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
MODULE_PATH = ROOT / "scripts" / "password-cracking" / "hash-cracker.py"


def load_module():
    spec = importlib.util.spec_from_file_location("hash_cracker", MODULE_PATH)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class TestHashCracker(unittest.TestCase):
    def test_hash_word_md5(self):
        module = load_module()
        self.assertEqual(
            module.hash_word("password"),
            "5f4dcc3b5aa765d61d8327deb882cf99",
        )


if __name__ == "__main__":
    unittest.main()
