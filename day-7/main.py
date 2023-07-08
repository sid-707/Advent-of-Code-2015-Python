from circuit import Circuit

circuit = Circuit()

with open("input.txt", "r") as f:
    instructions = f.readlines()
    
    for instruction in instructions:
        circuit.read_instruction(instruction.strip())

print('part 1')
circuit.turn_on()
wire_a_signal = circuit.get_signals()['a']
print(wire_a_signal)
print()
print('part 2')
instructions = circuit.get_instructions()
instructions['b'] = {
    'operation': None,
    'operand_1': str(wire_a_signal)
}
circuit.set_instructions(instructions)
circuit.reset_signals()
circuit.turn_on()
print(circuit.get_signals()['a'])


    
