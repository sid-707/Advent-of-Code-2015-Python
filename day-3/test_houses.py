import unittest
from houses import count_number_of_houses


class TestHouses(unittest.TestCase):
    def test_1(self):
        self.assertEqual(count_number_of_houses('>'), 2)
    def test_2(self):
        self.assertEqual(count_number_of_houses('^>v<'), 4)
    def test_3(self):
        self.assertEqual(count_number_of_houses('^v^v^v^v^v'), 2)


if __name__ == "__main__":
    unittest.main()
