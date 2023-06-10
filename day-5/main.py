from scanner import is_string_nice

with open("input.txt", "r") as f:
    strings = f.readlines()
    
    num_nice_strings = 0
    for string in strings:
        if is_string_nice(string.strip()):
            num_nice_strings += 1

    print(num_nice_strings)
    
