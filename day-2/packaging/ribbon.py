from .formulas import get_perimeter, get_volume

def get_ribbon_amount(dimensions):
    l = dimensions["l"]
    w = dimensions['w']
    h = dimensions['h']
    min_dimension = dimensions['min_dimension']
    second_min_dimension = dimensions['second_min_dimension']
    return get_perimeter(min_dimension, second_min_dimension) + get_volume(l,w,h)
