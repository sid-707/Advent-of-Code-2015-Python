def is_string_nice(string):
    num_vowels = 0
    has_double_letter = False
    INVALID_SUBSTRINGS = ['ab', 'cd', 'pq', 'xy']
    has_invalid_substring = False
    for i, c in enumerate(string):
        if c in 'aeiou':
            num_vowels += 1
        if i != 0:
            if string[i-1] == string[i]:
                has_double_letter = True
            if string[i-1:i+1] in INVALID_SUBSTRINGS:
                has_invalid_substring = True
                break

    return num_vowels >= 3 and has_double_letter and not has_invalid_substring