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

    def get_total_brightness(self):
        brightness = 0

        for i in range(DIMENSIONS):
            for j in range(DIMENSIONS):
                brightness += self.__grid[i][j]

        return brightness
        
    def __turn_off(self, start, end):
        x0, y0 = self.__coords_to_int(start)
        x1, y1 = self.__coords_to_int(end)

        for i in range(x0, x1 + 1):
            for j in range(y0, y1 + 1):
                if self.__grid[i][j] > 0: self.__grid[i][j] -= 1
    
    def __turn_on(self, start, end):
        x0, y0 = self.__coords_to_int(start)
        x1, y1 = self.__coords_to_int(end)

        for i in range(x0, x1 + 1):
            for j in range(y0, y1 + 1):
                self.__grid[i][j] += 1
    
    def __toggle(self, start, end):
        x0, y0 = self.__coords_to_int(start)
        x1, y1 = self.__coords_to_int(end)

        for i in range(x0, x1 + 1):
            for j in range(y0, y1 + 1):
                self.__grid[i][j] += 2

    def read_instruction(self, instruction):
        words = instruction.split()

        if words[0] == 'turn':
            if words[1] == 'off':
                self.__turn_off(words[2], words[4])
            elif words[1] == 'on':
                self.__turn_on(words[2], words[4])
        elif words[0] == 'toggle':
            self.__toggle(words[1], words[3])
