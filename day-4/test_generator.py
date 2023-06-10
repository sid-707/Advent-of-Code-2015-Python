import unittest
from generator import get_smallest_number


class TestGeneratorMethod(unittest.TestCase):
    def test_1(self):
        self.assertEqual(get_smallest_number('abcdef'), 609043)

    def test_2(self):
        self.assertEqual(get_smallest_number('pqrstuv'), 1048970)
    
    def test_3(self):
        self.assertEqual(get_smallest_number('yzbqklnj'), 282749)

    def test_4(self):
        self.assertEqual(get_smallest_number('yzbqklnj', 6), 9962624)


if __name__ == "__main__":
    unittest.main()
