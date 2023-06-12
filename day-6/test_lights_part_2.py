import unittest
from lights_part_2 import Lights, DIMENSIONS


class TestLights2(unittest.TestCase):
    def setUp(self):
        self.lights = Lights(DIMENSIONS)

    def test_1(self):
        self.lights.read_instruction('toggle 0,0 through 999,999')
        self.assertEqual(self.lights.get_total_brightness(), 2000000)


if __name__ == "__main__":
    unittest.main()
