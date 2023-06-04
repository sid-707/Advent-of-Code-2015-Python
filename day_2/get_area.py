def get_area(dimensions):
    l, w, h = [int(i) for i in dimensions.split("x")]

    sorted_dimensions = sorted([l, w, h])
    min_value = min(sorted_dimensions)
    second_min_value = sorted_dimensions[1]

    return 2 * l * w + 2 * w * h + 2 * h * l + min_value * second_min_value
