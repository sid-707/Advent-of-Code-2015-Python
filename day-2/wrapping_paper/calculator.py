def get_wrapping_paper_amount(dimensions):
    l = dimensions['l']
    w = dimensions['w']
    h = dimensions['h']
    min_dimension = dimensions['min_dimension']
    second_min_dimension = dimensions['second_min_dimension']

    return 2 * l * w + 2 * w * h + 2 * h * l + min_dimension * second_min_dimension
