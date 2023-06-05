def get_floor(instructions: str):
    floor = 0
    entered_basement_position = None

    for i, c in enumerate(instructions):
        if c == "(":
            floor += 1
        if c == ")":
            floor -= 1

            if floor == -1 and entered_basement_position == None:
                entered_basement_position = i + 1

    return {"floor": floor, "entered_basement_position": entered_basement_position}
