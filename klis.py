CACHELEN = []
CACHECNT = []


def reconstruct(start, skip, result, target):
    if start != 0:
        result.append(str(target[start]))
    followers = []
    for next_cur in range(start + 1, len(target)):
        if (start == 0 or target[start] < target[next_cur]) and\
                lis(start, target) == lis(next_cur, target) + 1:
            followers.append([target[next_cur], next_cur])
    followers.sort()
    for i in range(len(followers)):
        idx = followers[i][1]
        cnt = count(idx, target)
        if cnt <= skip:
            skip -= cnt
        else:
            reconstruct(idx, skip, result, target)
            break


def lis(start, target):
    global CACHELEN
    if CACHELEN[start] != -1:
        return CACHELEN[start]
    CACHELEN[start] = 1
    for next_cur in range(start + 1, len(target)):
        if start == 0 or target[start] < target[next_cur]:
            CACHELEN[start] = max(
                CACHELEN[start], lis(next_cur, target) + 1)
    return CACHELEN[start]


def count(start, target):
    global CACHECNT
    if lis(start, target) == 1:
        return 1
    if CACHECNT[start] != -1:
        return CACHECNT[start]
    CACHECNT[start] = 0
    for next_cur in range(start + 1, len(target)):
        if (start == 0 or target[start] < target[next_cur]) and\
                lis(start, target) == lis(next_cur, target) + 1:
            CACHECNT[start] = \
                CACHECNT[start] + count(next_cur, target)
    return CACHECNT[start]


def klis(input_case):
    global CACHELEN, CACHECNT
    input_list = list(
        map(
            lambda x: [int(i) for i in x.strip().split(' ')],
            input_case.split('\n')
        )
    )
    case_num = input_list[0][0]
    input_list = input_list[1:]
    for i in range(case_num):
        skip = input_list[i*2][1]
        target = input_list[i*2 + 1]
        target.insert(0, -float('INF'))
        CACHELEN = [-1 for i in range(len(target))]
        CACHECNT = [-1 for i in range(len(target))]
        count(0, target)
        result = []
        reconstruct(0, skip - 1, result, target)
        print len(result)
        print ' '.join(result)


if __name__ == '__main__':
    input_case = \
        '''3
        8 6
        5 1 6 4 3 2 8 7
        8 4
        2 1 4 3 6 5 8 7
        8 2
        5 6 7 8 1 2 3 4'''
    klis(input_case)
