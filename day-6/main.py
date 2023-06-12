# from lights_part_1 import Lights, DIMENSIONS
from lights_part_2 import Lights, DIMENSIONS

lights = Lights(DIMENSIONS)

with open("input.txt", "r") as f:
    instructions = f.readlines()
    
    for instruction in instructions:
        lights.read_instruction(instruction)

    # part 1
    #print(lights.get_total_lights_on())

    # part 2
    print(lights.get_total_brightness())

    
