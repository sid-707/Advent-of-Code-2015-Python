from generator import get_smallest_number

with open("input.txt", "r") as f:
    str2hash = f.read()
    # print('i', get_smallest_number(str2hash))
    print('i with 6 zeros', get_smallest_number(str2hash, 6))
