import unittest
from scanner import is_string_nice_part_1, is_string_nice_part_2


class TestScannerMethodPart1(unittest.TestCase):
    def test_1(self):
        self.assertEqual(is_string_nice_part_1('ugknbfddgicrmopn'), True)

    def test_2(self):
        self.assertEqual(is_string_nice_part_1('aaa'), True)
    
    def test_3(self):
        self.assertEqual(is_string_nice_part_1('jchzalrnumimnmhp'), False)

    def test_4(self):
        self.assertEqual(is_string_nice_part_1('haegwjzuvuyypxyu'), False)
    
    def test_5(self):
        self.assertEqual(is_string_nice_part_1('dvszwmarrgswjxmb'), False)

class TestScannerMethodPart2(unittest.TestCase):
    def test_1(self):
        self.assertEqual(is_string_nice_part_2('qjhvhtzxzqqjkmpb'), True)

    def test_2(self):
        self.assertEqual(is_string_nice_part_2('xxyxx'), True)
    
    def test_3(self):
        self.assertEqual(is_string_nice_part_2('uurcxstgmygtbstg'), False)

    def test_4(self):
        self.assertEqual(is_string_nice_part_2('ieodomkazucvgmuy'), False)
    
    def test_5(self):
        self.assertEqual(is_string_nice_part_2('aaa'), False)


if __name__ == "__main__":
    unittest.main()
