import unittest
from .generator import get_dimensions_dict


class TestGeneratorMethod(unittest.TestCase):
    def test_1(self):
        dimensions = {
            "l": 2,
            "w": 3,
            "h": 4,
            "min_dimension": 2,
            "second_min_dimension": 3
        }
        self.assertDictEqual(get_dimensions_dict('2x3x4'), dimensions)

    def test_2(self):
        dimensions = {
            "l": 1,
            "w": 1,
            "h": 10,
            "min_dimension": 1,
            "second_min_dimension": 1
        }
        self.assertDictEqual(get_dimensions_dict('1x1x10'), dimensions)


if __name__ == "__main__":
    unittest.main()
