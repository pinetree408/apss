MOD = 10*1000*1000
CACHE = [[]]


def _poly(n, first):
    global CACHE
    if n == first:
        return 1
    if CACHE[n][first] != -1:
        return CACHE[n][first]
    CACHE[n][first] = 0
    for second in range(1, n-first+1):
        add = second + first - 1
        add = add * _poly(n - first, second)
        add = add % MOD
        CACHE[n][first] = CACHE[n][first] + add
        CACHE[n][first] = CACHE[n][first] % MOD
    return CACHE[n][first]


def poly(input_case):
    global CACHE
    input_list = list(
        map(
            lambda x: [int(i) for i in x.strip().split(' ')],
            input_case.split('\n')
        )
    )
    case_num = input_list[0][0]
    input_list = input_list[1:]
    for i in range(case_num):
        n = input_list[i][0]
        CACHE = [[-1 for j in range(n + 1)] for i in range(n + 1)]
        result = 0
        for j in range(1, n+1):
            result = result + _poly(n, j)
            result = result % MOD
        print result


if __name__ == '__main__':
    input_case = \
        '''3
        2
        4
        92'''
    poly(input_case)
