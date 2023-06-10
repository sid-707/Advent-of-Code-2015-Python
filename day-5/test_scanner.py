import unittest
from scanner import is_string_nice


class TestScannerMethod(unittest.TestCase):
    def test_1(self):
        self.assertEqual(is_string_nice('ugknbfddgicrmopn'), True)

    def test_2(self):
        self.assertEqual(is_string_nice('aaa'), True)
    
    def test_3(self):
        self.assertEqual(is_string_nice('jchzalrnumimnmhp'), False)

    def test_4(self):
        self.assertEqual(is_string_nice('haegwjzuvuyypxyu'), False)
    
    def test_5(self):
        self.assertEqual(is_string_nice('dvszwmarrgswjxmb'), False)


if __name__ == "__main__":
    unittest.main()
