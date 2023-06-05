def __get_volume(l,w,h):
    return l*w*h

def __get_perimeter(side_1, side_2):
    return side_1*2 + side_2*2

def get_ribbon_amount(dimensions):
    l = dimensions["l"]
    w = dimensions['w']
    h = dimensions['h']
    min_dimension = dimensions['min_dimension']
    second_min_dimension = dimensions['second_min_dimension']
    return __get_perimeter(min_dimension, second_min_dimension) + __get_volume(l,w,h)
