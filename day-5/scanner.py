import math

def is_string_nice_part_1(string):
    num_vowels = 0
    has_double_letter = False
    INVALID_SUBSTRINGS = {'ab', 'cd', 'pq', 'xy'}
    VOWELS = { 'a', 'e', 'i', 'o', 'u' }

    has_invalid_substring = False
    for i, c in enumerate(string):
        if c in VOWELS:
            num_vowels += 1
        if i != 0:
            if string[i-1] == string[i]:
                has_double_letter = True
            if string[i-1:i+1] in INVALID_SUBSTRINGS:
                has_invalid_substring = True
                break

    return num_vowels >= 3 and has_double_letter and not has_invalid_substring

def is_string_nice_part_2(string):
    substrings = {}
    has_pair_two_letters = False
    has_repeating_letter = False
    for i, _ in enumerate(string):
        if i >= 1:
            two_letters = string[i-1:i+1]
            if two_letters not in substrings:
                substrings[two_letters] = i
            elif substrings[two_letters] != i - 1: # Skip overlap
                has_pair_two_letters = True

        if i >= 2 and string[i - 2] == string[i]:
            has_repeating_letter = True

    return has_pair_two_letters and has_repeating_letter