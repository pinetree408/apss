COVERED = [[]]
BEST = 0


def remove_duplicate_rotations(rotations):
    new_rotations = []
    for rotation in rotations:
        if len(new_rotations) == 0:
            new_rotations.append(rotation)
        else:
            duplicate_count = 0
            for new_rotation in new_rotations:
                second_count = 0
                for i in range(len(rotation)):
                    first_count = 0
                    for j in range(len(rotation[i])):
                        if new_rotation[i][j] == rotation[i][j]:
                            first_count = first_count + 1
                    if first_count == len(rotation[i]):
                        second_count = second_count + 1
                if second_count == len(rotation):
                    duplicate_count = duplicate_count + 1
            if duplicate_count == 0:
                new_rotations.append(rotation)
    return new_rotations


def rotate(block):
    ret = [['' for i in range(len(block))] for j in range(len(block[0]))]
    for i in range(len(block)):
        for j in range(len(block[0])):
            ret[j][len(block) - i - 1] = block[i][j]
    return ret


def generate_rotations(block):
    rotations = [[] for i in range(4)]
    for rot in range(4):
        origin_y = -1
        origin_x = -1
        for i in range(len(block)):
            for j in range(len(block[i])):
                if block[i][j] == '#':
                    if origin_y == -1:
                        origin_y = i
                        origin_x = j
                    rotations[rot].append([
                        i - origin_y,
                        j - origin_x
                    ])
        block = rotate(block)
    return remove_duplicate_rotations(rotations)


def search(placed, rotations):
    global COVERED, BEST
    y = -1
    x = -1
    for r in range(len(COVERED)):
        for c in range(len(COVERED[r])):
            if COVERED[r][c] == 0:
                y = r
                x = c
                break
        if y != -1:
            break
    if y == -1:
        BEST = max(BEST, placed)
        return
    for i in range(len(rotations)):
        set_flag = True
        for j in rotations[i]:
            if (0 <= y+j[0] < len(COVERED))\
                    and (0 <= x+j[1] < len(COVERED[0])):
                if COVERED[y+j[0]][x+j[1]] == 1:
                    set_flag = False
                COVERED[y+j[0]][x+j[1]] = COVERED[y+j[0]][x+j[1]]+1
            else:
                set_flag = False
        if set_flag:
            search(placed + 1, rotations)
        for j in rotations[i]:
            if (0 <= y+j[0] < len(COVERED))\
                    and (0 <= x+j[1] < len(COVERED[0])):
                COVERED[y+j[0]][x+j[1]] = COVERED[y+j[0]][x+j[1]]-1
    COVERED[y][x] = 1
    search(placed, rotations)
    COVERED[y][x] = 0


def boardcover(input_case):
    global COVERED, BEST
    input_list = list(
        map(
            lambda x: x.strip(),
            input_case.split('\n')
        )
    )
    case_num = int(input_list[0])
    input_list = input_list[1:]
    case_start = 0
    for i in range(case_num):
        start = case_start
        area_info = input_list[start].split(' ')
        height = int(area_info[0])
        block_row = int(area_info[2])
        map_end = start + height
        board = input_list[start + 1:map_end + 1]
        block = input_list[map_end + 1:map_end + block_row + 1]
        rotations = generate_rotations(block)
        COVERED = [
            [0 for c in range(len(board[r]))] for r in range(len(board))
        ]
        for r in range(len(board)):
            for c in range(len(board[r])):
                if board[r][c] == '#':
                    COVERED[r][c] = 1
        BEST = 0
        search(0, rotations)
        print BEST
        case_start = map_end + block_row + 1


if __name__ == '__main__':
    input_case = \
        '''2
        4 7 2 3
        ##.##..
        #......
        #....##
        #..####
        ###
        #..
        5 10 3 3
        ..........
        ..........
        ..........
        ..........
        ..........
        .#.
        ###
        ..#'''
    boardcover(input_case)
