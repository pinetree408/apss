CACHE = [[]]


def _num3r(here, days, n, p, connected, deg):
    global CACHE
    if days == 0:
        return 1.0 if here == p else 0.0
    if CACHE[here][days] > -0.5:
        return CACHE[here][days]
    CACHE[here][days] = 0.0
    for there in range(n):
        if connected[here][there] == 1:
            CACHE[here][days] = CACHE[here][days] +\
                (_num3r(there, days-1, n, p, connected, deg) / deg[there])
    return CACHE[here][days]


def numb3r(input_case):
    global CACHE
    input_list = list(
        map(
            lambda x: [int(i) for i in x.strip().split(' ')],
            input_case.split('\n')
        )
    )
    case_num = input_list[0][0]
    input_list = input_list[1:]
    cursor = 0
    for i in range(case_num):
        n = input_list[i + cursor][0]
        d = input_list[i + cursor][1]
        p = input_list[i + cursor][2]
        connected = input_list[i + cursor + 1:i + cursor + 1 + n]
        t = input_list[i + cursor + 1 + n + 1]
        cursor = n + 2
        CACHE = [[-1 for j in range(d + 1)] for i in range(n)]
        deg = [0 for i in range(n)]
        for i in range(n):
            for j in range(n):
                if connected[i][j] == 1:
                    deg[i] = deg[i] + 1
        result = []
        for here in t:
            result.append(str(_num3r(here, d, n, p, connected, deg)))
        print ' '.join(result)


if __name__ == '__main__':
    input_case = \
        '''2
        5 2 0
        0 1 1 1 0
        1 0 0 0 1
        1 0 0 0 0
        1 0 0 0 0
        0 1 0 0 0
        3
        0 2 4
        8 2 3
        0 1 1 1 0 0 0 0
        1 0 0 1 0 0 0 0
        1 0 0 1 0 0 0 0
        1 1 1 0 1 1 0 0
        0 0 0 1 0 0 1 1
        0 0 0 1 0 0 0 1
        0 0 0 0 1 0 0 0
        0 0 0 0 1 1 0 0
        4
        3 1 2 6'''
    numb3r(input_case)
