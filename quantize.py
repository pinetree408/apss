CACHE = [[]]


def min_error(start, end, source):
    p_sum = sum(source[start:end+1])
    m = round(p_sum*1.0/(end - start + 1))
    errors = list(
        map(
            lambda x: (x-m)*(x-m),
            source[start:end+1]
        )
    )
    return sum(errors)


def _quantize(start, parts, source):
    global CACHE
    if start == len(source):
        return 0
    if parts == 0:
        return float('Inf')
    if CACHE[start][parts] != -1:
        return CACHE[start][parts]
    CACHE[start][parts] = float('Inf')
    for part_size in range(1, len(source) - start + 1):
        CACHE[start][parts] = min(
            CACHE[start][parts],
            min_error(start, start + part_size - 1, source) +
            _quantize(start + part_size, parts - 1, source)
        )
    return CACHE[start][parts]


def quantize(input_case):
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
        parts = input_list[i*2][1]
        target = list(
            map(
                lambda x: int(x),
                input_list[i*2 + 1]
            )
        )
        target.sort()
        CACHE = [[-1 for j in range(parts+1)] for i in range(len(target)+1)]
        print _quantize(0, parts, target)


if __name__ == '__main__':
    input_case = \
        '''2
        10 3
        3 3 3 1 2 3 2 2 2 1
        9 3
        1 744 755 4 897 902 890 6 777'''
    quantize(input_case)
