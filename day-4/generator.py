import hashlib

def get_smallest_number(secret_key, num_of_starting_zeros = 5):
    result = ''
    startsWith = num_of_starting_zeros * '0'
    i = 0
    while True:
        word = secret_key+str(i)
        result = hashlib.md5(word.encode()).hexdigest()
        
        if result[:num_of_starting_zeros] == startsWith:
            break
        i += 1
    return i