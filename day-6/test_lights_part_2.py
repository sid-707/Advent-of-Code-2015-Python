import unittest
from lights_part_2 import Lights, DIMENSIONS


class TestLights2(unittest.TestCase):
    def setUp(self):
        self.lights = Lights(DIMENSIONS)
        self.lights.reset()

    def test_turn_on(self):
        self.lights.read_instruction('turn on 0,0 through 999,999')

        lights = self.lights.get_lights()

        for i in range(DIMENSIONS):
            for j in range(DIMENSIONS):
                self.assertEqual(lights[i][j], 1)

    def test_toggle(self):
        self.lights.read_instruction('toggle 0,0 through 999,999')

        lights = self.lights.get_lights()

        for i in range(DIMENSIONS):
            for j in range(DIMENSIONS):
                self.assertEqual(lights[i][j], 2)

    def test_turn_off(self):
        self.lights.read_instruction('toggle 0,0 through 999,999')
        self.lights.read_instruction('turn off 0,0 through 999,999')

        lights = self.lights.get_lights()

        for i in range(DIMENSIONS):
            for j in range(DIMENSIONS):
                self.assertEqual(lights[i][j], 1)

    def test_get_total_brightness(self):
        self.lights.read_instruction('toggle 0,0 through 999,999')
        self.assertEqual(self.lights.get_total_brightness(), 2000000)


if __name__ == "__main__":
    unittest.main()
