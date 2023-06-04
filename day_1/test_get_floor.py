import unittest
from get_floor import get_floor


class TestStringMethods(unittest.TestCase):
    def test_1(self):
        self.assertDictEqual(
            get_floor("(())"), {"floor": 0, "entered_basement_position": None}
        )

    def test_2(self):
        self.assertDictEqual(
            get_floor("()()"), {"floor": 0, "entered_basement_position": None}
        )

    def test_3(self):
        self.assertDictEqual(
            get_floor("((("), {"floor": 3, "entered_basement_position": None}
        )

    def test_4(self):
        self.assertDictEqual(
            get_floor("(()(()("), {"floor": 3, "entered_basement_position": None}
        )

    def test_4(self):
        self.assertDictEqual(
            get_floor("))((((("), {"floor": 3, "entered_basement_position": 1}
        )

    def test_5(self):
        self.assertDictEqual(
            get_floor("())"), {"floor": -1, "entered_basement_position": 3}
        )

    def test_6(self):
        self.assertDictEqual(
            get_floor("))("), {"floor": -1, "entered_basement_position": 1}
        )

    def test_7(self):
        self.assertDictEqual(
            get_floor(")))"), {"floor": -3, "entered_basement_position": 1}
        )

    def test_8(self):
        self.assertDictEqual(
            get_floor(")())())"), {"floor": -3, "entered_basement_position": 1}
        )


if __name__ == "__main__":
    unittest.main()
