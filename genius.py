CACHE = [[]]


def get_prob(k, n, duration, prob):
    global CACHE
    CACHE[0][0] = 1.0
    for time in range(1, k+1):
        for song in range(n):
            CACHE[time % 5][song] = 0
            for last in range(n):
                CACHE[time % 5][song] = CACHE[time % 5][song] +\
                    (
                        CACHE[(time-duration[last]+5) % 5][last] *
                        prob[last][song]
                    )
    ret = [0 for i in range(n)]
    for song in range(n):
        for start in range(k-duration[song]+1, k+1):
            ret[song] = ret[song] + CACHE[start % 5][song]
    return ret


def genius(input_case):
    global CACHE
    input_list = list(
        map(
            lambda x: [float(i) for i in x.strip().split(' ')],
            input_case.split('\n')
        )
    )
    case_num = int(input_list[0][0])
    input_list = input_list[1:]
    cursor = 0
    for i in range(case_num):
        n = int(input_list[cursor][0])
        k = int(input_list[cursor][1])
        duration = list(
            map(
                lambda x: int(x),
                input_list[cursor+1]
            )
        )
        prob = input_list[cursor+2:cursor+2+n]
        like_list = list(
            map(
                lambda x: int(x),
                input_list[cursor+2+n]
            )
        )
        CACHE = [[0.0 for s in range(n)] for t in range(4 + 1)]
        ret = get_prob(k, n, duration, prob)
        sorted_ret = []
        for like in like_list:
            sorted_ret.append(ret[like])
        print sorted_ret
        cursor = cursor + 2 + n + 1


if __name__ == '__main__':
    input_case = \
        '''3
        3 6 3
        4 4 2
        0.18 0.40 0.42
        0.15 0.46 0.39
        0.58 0.23 0.19
        0 1 2
        4 10 4
        1 3 2 4
        0.26 0.07 0.49 0.18
        0.21 0.33 0.15 0.31
        0.41 0.20 0.38 0.01
        0.28 0.31 0.18 0.23
        2 0 3 1
        4 1000 4
        4 3 4 4
        0.08 0.47 0.12 0.33
        0.10 0.02 0.39 0.49
        0.08 0.33 0.35 0.24
        0.14 0.19 0.58 0.09
        1 3 2 0'''
    genius(input_case)
