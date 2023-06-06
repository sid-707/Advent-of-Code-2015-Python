from packaging import get_wrapping_paper_amount, get_ribbon_amount
from utils import get_dimensions_dict

total_wrapping_paper_amount = 0
total_ribbon_amount = 0

with open("input.txt", "r") as f:
    dimensions_lines = f.readlines()

    for dimensions_line in dimensions_lines:
        dimensions_dict = get_dimensions_dict(dimensions_line)

        total_wrapping_paper_amount += get_wrapping_paper_amount(dimensions_dict)
        total_ribbon_amount += get_ribbon_amount(dimensions_dict)
    

print('total_wrapping_paper_amount', total_wrapping_paper_amount)
print('total_wrapping_ribbon_amount', total_ribbon_amount)