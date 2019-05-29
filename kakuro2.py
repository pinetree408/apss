CANDIDATES = [[[]]]
N = 0
MAXN = 20
COLOR = [[0 for i in range(MAXN)] for j in range(MAXN)]
VALUE = [[0 for i in range(MAXN)] for j in range(MAXN)]
HINT = [[[0 for k in range(2)] for i in range(MAXN)] for j in range(MAXN)]
Q = 0
SUM = [0 for i in range(MAXN * MAXN)]
LENGTH = [0 for i in range(MAXN * MAXN)]
KNOWN = [0 for i in range(MAXN * MAXN)]


def put(y, x, val):
    global KNOWN, HINT, VALUE
    for h in range(2):
        KNOWN[HINT[y][x][h]] = KNOWN[HINT[y][x][h]] + (1 << val)
    VALUE[y][x] = val


def remove(y, x, val):
    global KNOWN, HINT, VALUE
    for h in range(2):
        KNOWN[HINT[y][x][h]] = KNOWN[HINT[y][x][h]] - (1 << val)
    VALUE[y][x] = 0


def get_cand_hint(hint):
    global CANDIDATES, LENGTH, SUM, KNOWN
    return CANDIDATES[LENGTH[hint]][SUM[hint]][KNOWN[hint]]


def get_cand_coord(y, x):
    global HINT
    return (get_cand_hint(HINT[y][x][0]) & get_cand_hint(HINT[y][x][1]))


def get_size(mask):
    size = 0
    compare = 1
    for i in range(1, 10):
        compare = compare << 1
        if compare & mask:
            size = size + 1
    return size


def get_sum(mask):
    mask_sum = 0
    compare = 1
    for i in range(1, 10):
        compare = compare << 1
        if compare & mask:
            mask_sum = mask_sum + i
    return mask_sum


def generate_candidates():
    global CANDIDATES
    CANDIDATES = [
        [
            [
                0 for k in range(1024)
            ] for j in range(46)
        ] for i in range(10)
    ]
    for i in range(0, 1024, 2):
        l = get_size(i)
        s = get_sum(i)
        sub_s = i
        while True:
            CANDIDATES[l][s][sub_s] = CANDIDATES[l][s][sub_s] | (i & ~sub_s)
            if sub_s == 0:
                break
            sub_s = (sub_s - 1) & i


def search():
    global N, COLOR, VALUE
    y = -1
    x = -1
    min_cand = 1023
    for i in range(N):
        for j in range(N):
            if COLOR[i][j] == 1 and VALUE[i][j] == 0:
                cand = get_cand_coord(i, j)
                if get_size(min_cand) > get_size(cand):
                    min_cand = cand
                    y = i
                    x = j
    if min_cand == 0:
        return False
    if y == -1:
        for i in range(N):
            print VALUE[i][:N]
        return True
    for val in range(1, 10):
        if min_cand & (1 << val):
            put(y, x, val)
            if search():
                return True
            remove(y, x, val)
    return False


def kakuro(input_case):
    global N, COLOR, VALUE, HINT, SUM, LENGTH
    input_list = list(
        map(
            lambda x: [int(i) for i in x.strip().split(' ')],
            input_case.split('\n')
        )
    )
    case_num = input_list[0][0]
    input_list = input_list[1:]
    case_start = 0
    for i in range(case_num):
        start = case_start
        map_size = input_list[start][0]
        map_list = input_list[start+1:start+1+map_size]
        hint_num = input_list[start+1+map_size][0]
        hint_list = input_list[
            start+1+map_size+1:start+1+map_size+hint_num+1
        ]
        generate_candidates()
        N = map_size
        for i in range(N):
            for j in range(N):
                COLOR[i][j] = map_list[i][j]
                VALUE[i][j] = 0
        for k, hint in enumerate(hint_list):
            HINT[hint[0]-1][hint[1]-1][hint[2]] = k
            SUM[HINT[hint[0]-1][hint[1]-1][hint[2]]] = hint[3]
            simul_y = 0
            simul_x = 1
            if hint[2] == 1:
                simul_y = 1
                simul_x = 0
            length = 0
            while True:
                if COLOR[hint[0]-1+simul_y][hint[1]-1+simul_x] == 0:
                    break
                HINT[hint[0]-1+simul_y][hint[1]-1+simul_x][hint[2]] = k
                length = length + 1
                if hint[2] == 0:
                    simul_x = simul_x + 1
                elif hint[2] == 1:
                    simul_y = simul_y + 1
            LENGTH[HINT[hint[0]-1][hint[1]-1][hint[2]]] = length
        search()
        case_start = start+1+map_size+hint_num+1


if __name__ == '__main__':
    input_case = \
        '''1
        8
        0 0 0 0 0 0 0 0
        0 1 1 0 0 1 1 1
        0 1 1 0 1 1 1 1
        0 1 1 1 1 1 0 0
        0 0 1 1 0 1 1 0
        0 0 0 1 1 1 1 1
        0 1 1 1 1 0 1 1
        0 1 1 1 0 0 1 1
        24
        2 1 0 16
        2 5 0 24
        3 1 0 17
        3 4 0 29
        4 1 0 35
        5 2 0 7
        5 5 0 8
        6 3 0 16
        7 1 0 21
        7 6 0 5
        8 1 0 6
        8 6 0 3
        1 2 1 23
        1 3 1 30
        1 6 1 27
        1 7 1 12
        1 8 1 16
        2 5 1 17
        3 4 1 15
        4 7 1 12
        5 5 1 7
        5 8 1 7
        6 2 1 11
        6 3 1 10'''
    kakuro(input_case)
