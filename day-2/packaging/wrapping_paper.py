from .formulas import get_surface_area

def get_wrapping_paper_amount(dimensions):
    l = dimensions['l']
    w = dimensions['w']
    h = dimensions['h']
    min_dimension = dimensions['min_dimension']
    second_min_dimension = dimensions['second_min_dimension']

    return get_surface_area(l, w, h) + min_dimension * second_min_dimension
