import collections


def is_dominated(x, y, coords):
    idx = 0
    sorted_coords = collections.OrderedDict(sorted(coords.items()))
    for i, key in enumerate(sorted_coords.keys()):
        idx = i
        if key > x:
            break
    if len(sorted_coords.keys()) == 0 or idx == len(sorted_coords.keys())-1:
        return False
    return y < coords[sorted_coords.keys()[idx]]


def remove_dominated(x, y, coords):
    idx = 0
    sorted_coords = collections.OrderedDict(sorted(coords.items()))
    for i, key in enumerate(sorted_coords.keys()):
        idx = i
        if key > x:
            if idx != 0:
                idx = idx-1
            break
    if idx == 0:
        return
    while True:
        if coords[sorted_coords.keys()[idx]] > y:
            break
        if idx == 0:
            coords.pop(sorted_coords.keys()[idx], None)
            break
        else:
            new_idx = idx
            new_idx = new_idx-1
            coords.pop(sorted_coords.keys()[idx], None)
            idx = new_idx


def registered(x, y, coords):
    if is_dominated(x, y, coords):
        return len(coords.key())
    remove_dominated(x, y, coords)
    coords[x] = y
    return len(coords.keys())


def solve(people):
    ret = 0
    coords = {}
    for person in people:
        ret = ret+registered(person[0], person[1], coords)
    return ret


def nerd2(input_case):
    input_list = list(
        map(
            lambda x: [float(i) for i in x.strip().split(' ')],
            input_case.split('\n')
        )
    )
    case_num = int(input_list[0][0])
    input_list = input_list[1:]

    case_start = 0
    for i in range(case_num):
        start = case_start
        people_num = int(input_list[start][0])
        people_list = input_list[start+1:start+1+people_num]
        print solve(people_list)
        case_start = start+1+people_num


if __name__ == '__main__':
    input_case = \
        '''2
        4
        72 50
        57 67
        74 55
        64 60
        5
        1 5
        2 4
        3 3
        4 2
        5 1'''
    nerd2(input_case)
