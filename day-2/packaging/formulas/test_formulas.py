import unittest
from .formulas import get_surface_area, get_perimeter, get_volume

class TestFormulas(unittest.TestCase):
    def test_get_surface_area(self):
        self.assertEqual(get_surface_area(2, 3, 4), 52)

    def test_get_perimeter(self):
        self.assertEqual(get_perimeter(2, 3), 10)

    def test_get_volume(self):
        self.assertEqual(get_volume(2, 3, 4), 24)

if __name__ == "__main__":
    unittest.main()
