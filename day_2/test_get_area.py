import unittest
from get_area import get_area


class TestStringMethods(unittest.TestCase):
    def test_1(self):
        self.assertEqual(get_area("2x3x4"), 58)

    def test_2(self):
        self.assertEqual(get_area("1x1x10"), 43)


if __name__ == "__main__":
    unittest.main()
