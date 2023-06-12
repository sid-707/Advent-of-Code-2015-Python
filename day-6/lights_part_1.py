DIMENSIONS = 1000

class Lights:
    __grid = []
    def __init__(self, dimensions):
        for x in range(dimensions):
            self.__grid.append([0] * dimensions)

    def __coords_to_int(self, coords):
        return [int(x) for x in coords.split(',')]

    def get_lights(self):
        return self.__grid

    def get_total_lights_on(self):
        num_lights_on = 0

        for i in range(DIMENSIONS):
            for j in range(DIMENSIONS):
                if self.__grid[i][j] == 1:
                    num_lights_on += 1

        return num_lights_on
    
    def __turn_off(self, start, end):
        x0, y0 = self.__coords_to_int(start)
        x1, y1 = self.__coords_to_int(end)

        for i in range(x0, x1 + 1):
            for j in range(y0, y1 + 1):
                self.__grid[i][j] = 0
    
    def __turn_on(self, start, end):
        x0, y0 = self.__coords_to_int(start)
        x1, y1 = self.__coords_to_int(end)

        for i in range(x0, x1 + 1):
            for j in range(y0, y1 + 1):
                self.__grid[i][j] = 1
    
    def __toggle(self, start, end):
        x0, y0 = self.__coords_to_int(start)
        x1, y1 = self.__coords_to_int(end)

        for i in range(x0, x1 + 1):
            for j in range(y0, y1 + 1):
                self.__grid[i][j] = int(self.__grid[i][j] == 0)

    def read_instruction(self, instruction):
        words = instruction.split()

        if words[0] == 'turn':
            if words[1] == 'off':
                self.__turn_off(words[2], words[4])
            elif words[1] == 'on':
                self.__turn_on(words[2], words[4])
        elif words[0] == 'toggle':
            self.__toggle(words[1], words[3])
