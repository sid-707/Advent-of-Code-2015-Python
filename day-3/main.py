from houses import count_number_of_houses

with open("input.txt", "r") as f:
    moves = f.read()

    print(count_number_of_houses(moves))