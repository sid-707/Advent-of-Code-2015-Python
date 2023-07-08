import unittest
from circuit import Circuit

instructions = {'x': {'operation': None, 'operand_1': '123'}, 'y': {'operation': None, 'operand_1': '456'}, 'd': {'operand_1': 'x', 'operation': 'AND', 'operand_2': 'y'}, 'e': {'operand_1': 'x', 'operation': 'OR', 'operand_2': 'y'}, 'f': {'operand_1': 'x', 'operation': 'LSHIFT', 'operand_2': '2'}, 'g': {'operand_1': 'y', 'operation': 'RSHIFT', 'operand_2': '2'}, 'h': {'operation': 'NOT', 'operand_1': 'x'}, 'i': {'operation': 'NOT', 'operand_1': 'y'}}
expectedSignals = {'x': 123, 'y': 456, 'd': 72, 'e': 507, 'f': 492, 'g': 114, 'h': 65412, 'i': 65079}

class TestCircuit(unittest.TestCase):
    def setUp(self):
        self.testfile = open('test_input.txt')
        self.instructions = self.testfile.readlines()
        self.circuit = Circuit()
        for instruction in self.instructions:
            self.circuit.read_instruction(instruction.strip())

    def tearDown(self):
       self.testfile.close()

    def test_turn_on(self):
        self.circuit.turn_on()
        self.assertDictEqual(self.circuit.get_signals(), expectedSignals)

    def test_reset_signals(self):
        self.circuit.turn_on()
        self.circuit.reset_signals()
        self.assertEqual('x' not in self.circuit.get_signals(), True)

    def test_getter(self):
        self.assertDictEqual(self.circuit.get_instructions(), instructions)
    
    def test_setter(self):
        newInstructions = self.circuit.get_instructions()
        newInstructions['x']['operand_1'] = '456'
        self.circuit.set_instructions(newInstructions)
        self.assertDictEqual(self.circuit.get_instructions(), newInstructions)

if __name__ == "__main__":
    unittest.main()
