from get_area import get_area

total_area = 0

f = open("input.txt", "r")
dimensions = f.readlines()

for dimension in dimensions:
    total_area += get_area(dimension)

f.close()

print(total_area)
