import unittest
from calculator import get_ribbon_amount


class TestStringMethods(unittest.TestCase):
    def test_1(self):
        dimensions = {
            "l": 2,
            "w": 3,
            "h": 4,
            "min_dimension": 2,
            "second_min_dimension": 3
        }
        self.assertEqual(get_ribbon_amount(dimensions), 34)

    def test_2(self):
        dimensions = {
            "l": 1,
            "w": 1,
            "h": 10,
            "min_dimension": 1,
            "second_min_dimension": 1
        }
        self.assertEqual(get_ribbon_amount(dimensions), 14)


if __name__ == "__main__":
    unittest.main()
