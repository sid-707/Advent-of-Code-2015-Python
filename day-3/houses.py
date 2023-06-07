def count_number_of_houses(moves):
    current_position = [0, 0]

    number_of_houses = 1

    houses_visited = { '0,0' }
    for move in moves:
        match move:
            case '>':
                current_position[0] += 1
            case '<':
                current_position[0] -= 1
            case '^':
                current_position[1] += 1
            case 'v':
                current_position[1] -= 1
        current_pos_str = ','.join(str(x) for x in current_position)
        if current_pos_str not in houses_visited:
            number_of_houses += 1
            houses_visited.add(current_pos_str)

    return number_of_houses
