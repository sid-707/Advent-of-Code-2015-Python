from scanner import is_string_nice_part_1, is_string_nice_part_2

with open("input.txt", "r") as f:
    strings = f.readlines()
    
    num_nice_strings = 0
    for string in strings:
        # if is_string_nice_part_1(string.strip()):
        if is_string_nice_part_2(string.strip()):
            num_nice_strings += 1

    print(num_nice_strings)
    
