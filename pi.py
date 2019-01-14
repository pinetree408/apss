CACHE = []


def classify(start, end, source):
    target = source[start:end + 1]
    if target == target[0]*len(target):
        return 1
    progressive = True
    for i in range(len(target)-1):
        if (int(target[i+1]) - int(target[i])) !=\
                (int(target[1]) - int(target[0])):
            progressive = False
    if progressive and abs(int(target[1]) - int(target[0])) == 1:
        return 2
    alternating = True
    for i in range(len(target)):
        if int(target[i]) != int(target[i % 2]):
            alternating = False
    if alternating:
        return 4
    if progressive:
        return 5
    return 10


def memorize(start, source):
    global CACHE
    if (start == len(source)):
        return 0
    if (CACHE[start] != -1):
        return CACHE[start]
    CACHE[start] = float('Inf')
    for L in range(3, 6):
        if start + L <= len(source):
            CACHE[start] = min(
                CACHE[start],
                memorize(start + L, source) +
                classify(start, start + L - 1, source)
            )
    return CACHE[start]


def pi(input_case):
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
        target = str(input_list[i][0])
        CACHE = [-1 for i in range(len(target))]
        print memorize(0, target)


if __name__ == '__main__':
    input_case = \
        '''5
        12341234
        11111222
        12122222
        22222222
        12673939'''
    pi(input_case)
