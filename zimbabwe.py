MOD = 1000000007
CACHE = []


def price(index, n, taken, mod, less, e, digit, m):
    global CACHE
    if index == n:
        if (mod and less) == 0:
            return 1
        else:
            return 0

    if CACHE[taken][mod][less] != -1:
        return CACHE[taken][mod][less]

    CACHE[taken][mod][less] = 0
    for i in range(n):
        if (taken & (1 << i)) == 0:
            if (not less) and (e[index] < digit[i]):
                continue
            if (i > 0) and (digit[i-1] == digit[i])\
                    and ((taken & (1 << (i-1))) == 0):
                continue
            next_taken = taken | (1 << i)
            next_mod = (mod * 10 + digit[i]) % m
            next_less = less or (e[index] > digit[i])
            CACHE[taken][mod][less] = CACHE[taken][mod][less] +\
                price(index + 1, n,
                      next_taken, next_mod, next_less,
                      e, digit, m)
            CACHE[taken][mod][less] = CACHE[taken][mod][less] % MOD
    return CACHE[taken][mod][less]


def zimbabwe(input_case):
    global CACHE
    input_list = list(
        map(
            lambda x: x.strip(),
            input_case.split('\n')
        )
    )
    case_num = int(input_list[0])
    input_list = input_list[1:]

    for i in range(case_num):
        e = input_list[i].split(' ')[0]
        e = [int(e[z]) for z in range(len(e))]
        digit = e[:]
        digit.sort()
        n = len(e)
        m = int(input_list[i].split(' ')[1])
        CACHE = [
            [
                [-1 for k in range(2)] for j in range(20)
            ] for p in range(1 << 14)
        ]
        print e, digit, m
        print price(0, n, 0, 0, 0, e, digit, m) - 1


if __name__ == '__main__':
    input_case = \
        '''4
        321 3
        123 3
        422 2
        12738173912 7'''
    zimbabwe(input_case)
