from get_floor import get_floor

f = open("input.txt", "r")
instructions = f.read()
f.close()

print(get_floor(instructions))
