import ctypes

class Circuit:
    __instructions = {}
    __signals = {}

    def __convert_to_unsigned(self, value_str):
        value = int(value_str)
        if value < 0:
            return ctypes.c_uint16(value).value
        return value

    def __evaluate(self, wire):
        if isinstance(wire, int) or wire.isnumeric():
            return self.__convert_to_unsigned(wire)
    
        if wire in self.__signals:
            return self.__signals[wire]

        instruction = self.__instructions[wire]

        opt = instruction['operation']

        if opt == None:
            self.__signals[wire] = self.__evaluate(instruction['operand_1'])
        elif opt == 'AND':
            self.__signals[wire] = self.__evaluate(instruction['operand_1']) & self.__evaluate(instruction['operand_2'])
        elif opt == 'OR':
            self.__signals[wire] = self.__evaluate(instruction['operand_1']) | self.__evaluate(instruction['operand_2'])
        elif opt == 'LSHIFT':
            op1 = instruction['operand_1']
            op2 = instruction['operand_2']
            self.__signals[wire] = self.__evaluate(instruction['operand_1']) << self.__evaluate(instruction['operand_2'])
        elif opt == 'RSHIFT':
            op1 = instruction['operand_1']
            op2 = instruction['operand_2']
            self.__signals[wire] = self.__evaluate(instruction['operand_1']) >> self.__evaluate(instruction['operand_2'])
        elif opt == 'NOT':
            self.__signals[wire] = self.__evaluate(~self.__evaluate(instruction['operand_1']))
        
        return self.__signals[wire]

    def get_signals(self):
        return self.__signals

    def reset_signals(self):
        self.__signals = {}

    def turn_on(self):
        for wire in self.__instructions:
            self.__evaluate(wire)
    
    def get_instructions(self):
        return self.__instructions

    def set_instructions(self, instructions):
        self.__instructions = instructions

    def read_instruction(self, instruction):
        words = instruction.split(' ')

        if words[1] == '->':
            self.__instructions[words[2]] = {
                "operation": None,
                "operand_1": words[0]
            }
        elif words[2] == '->':
            self.__instructions[words[3]] = {
                "operation": 'NOT',
                "operand_1": words[1]
            }
        elif words[3] == '->':
            self.__instructions[words[4]] = {
                "operand_1": words[0],
                "operation": words[1],
                "operand_2": words[2]
            }