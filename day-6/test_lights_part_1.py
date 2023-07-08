import unittest
from lights_part_1 import Lights, DIMENSIONS


class TestLights1(unittest.TestCase):
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
        self.lights.read_instruction('toggle 0,0 through 999,0')

        lights = self.lights.get_lights()

        for i in range(DIMENSIONS):
            for j in range(DIMENSIONS):
                if j == 0: self.assertEqual(lights[i][j], 1)
                else: self.assertEqual(lights[i][j], 0)

    def test_turn_off(self):
        self.lights.read_instruction('turn off 0,1 through 999,1')

        lights = self.lights.get_lights()

        for i in range(DIMENSIONS):
            self.assertEqual(lights[i][1], 0)

    def test_get_total_lights_on(self):
        self.lights.read_instruction('turn on 0,0 through 2,2')

        num_lights_on = self.lights.get_total_lights_on()

        self.assertEqual(num_lights_on, 9)

if __name__ == "__main__":
    unittest.main()
