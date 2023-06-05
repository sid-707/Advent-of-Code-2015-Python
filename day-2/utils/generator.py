def get_dimensions_dict(dimensions_line):
    l, w, h = [int(i) for i in dimensions_line.split("x")]
    sorted_dimensions = sorted([l, w, h])
    min_dimension = min(sorted_dimensions)
    second_min_dimension = sorted_dimensions[1]

    return {
        "l": l,
        "w": w,
        "h": h,
        "min_dimension": min_dimension,
        "second_min_dimension": second_min_dimension
    }