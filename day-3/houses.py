def update_position(current_pos, move):
    match move:
        case '>':
            current_pos[0] += 1
        case '<':
            current_pos[0] -= 1
        case '^':
            current_pos[1] += 1
        case 'v':
            current_pos[1] -= 1
    
    return current_pos

def count_number_of_houses(moves):
    position = {
        0: [0,0], # santa
        1: [0,0] # robo
    }

    number_of_houses = 1

    houses_visited = { '0,0' }
    for (index, move) in enumerate(moves):
        new_pos = update_position(position[index % 2], move)
        current_pos_str = ','.join(str(x) for x in new_pos)
        if current_pos_str not in houses_visited:
            number_of_houses += 1
            houses_visited.add(current_pos_str)

    return number_of_houses
