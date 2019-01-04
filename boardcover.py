patch_list = [
    [[0, 0], [1, 0], [0, 1]],
    [[0, 0], [0, 1], [1, 1]],
    [[0, 0], [1, 0], [1, 1]],
    [[0, 0], [0, 1], [-1, 1]]
]


def set_patch(patch, case, x, y, covered):
    flag = True
    for block in patch:
        target_x = x + block[0]
        target_y = y + block[1]
        if (target_x < 0 or target_x >= case['width']) or \
                (target_y < 0 or target_y >= case['height']):
            flag = False
        else:
            case['map'][target_y][target_x] += covered
            if case['map'][target_y][target_x] > 1:
                flag = False
    return flag


def cover(case):
    x = -1
    y = -1
    result = 0
    for i in range(case['height']):
        for j in range(case['width']):
            if case['map'][i][j] == 0:
                x = j
                y = i
                break
        if y != -1:
            break
    if x == -1 and y == -1:
        return 1
    for patch in patch_list:
        if set_patch(patch, case, x, y, 1):
            result += cover(case)
        set_patch(patch, case, x, y, -1)

    return result


def boardcover(input_case):
    input_list = list(
        map(
            lambda x: x.strip(),
            input_case.split('\n')
        )
    )
    case_num = int(input_list[0])
    input_list = input_list[1:]
    case_start = 0
    case_list = []
    for i in range(case_num):
        start = case_start
        area_info = input_list[start].split(' ')
        width = int(area_info[1])
        height = int(area_info[0])
        end = start + height + 1
        map_list = input_list[start + 1:end]
        num_map_list = []
        count = 0
        for h in range(height):
            row = []
            for w in range(width):
                if map_list[h][w] == '.':
                    count += 1
                    row.append(0)
                else:
                    row.append(1)
            num_map_list.append(row)
        case = {
            'width': width,
            'height': height,
            'map': num_map_list,
            'count': count
        }
        case_list.append(case)
        case_start = end
    for case in case_list:
        result = 0
        if case['count'] % 3 == 0:
            result = cover(case)
        print result


if __name__ == '__main__':
    input_case = \
        '''3
        3 7
        #.....#
        #.....#
        ##...##
        3 7
        #.....#
        #.....#
        ##..###
        8 10
        ##########
        #........#
        #........#
        #........#
        #........#
        #........#
        #........#
        ##########'''
    boardcover(input_case)
