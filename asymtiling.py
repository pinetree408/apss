MOD = 1000000007
N = 100
CACHE_TILING = [-1 for i in range(N + 1)]
CACHE_ASYM = [-1 for i in range(N + 1)]


def tiling(width):
    global CACHE_TILING
    if width <= 1:
        return 1
    if CACHE_TILING[width] != -1:
        return CACHE_TILING[width]
    CACHE_TILING[width] = (tiling(width - 2) + tiling(width - 1)) % MOD
    return CACHE_TILING[width]


def _asymtiling(width):
    global CACHE_ASYM
    if width <= 2:
        return 0
    if CACHE_ASYM[width] != -1:
        return CACHE_ASYM[width]
    CACHE_ASYM[width] = _asymtiling(width - 2) % MOD
    CACHE_ASYM[width] = (CACHE_ASYM[width] + _asymtiling(width - 4)) % MOD
    CACHE_ASYM[width] = (CACHE_ASYM[width] + tiling(width - 3)) % MOD
    CACHE_ASYM[width] = (CACHE_ASYM[width] + tiling(width - 3)) % MOD
    return CACHE_ASYM[width]


def asymtiling(input_case):
    input_list = list(
        map(
            lambda x: [int(i) for i in x.strip().split(' ')],
            input_case.split('\n')
        )
    )
    case_num = input_list[0][0]
    input_list = input_list[1:]
    for i in range(case_num):
        width = input_list[i][0]
        print _asymtiling(width)


if __name__ == '__main__':
    input_case = \
        '''3
        2
        4
        92'''
    asymtiling(input_case)
