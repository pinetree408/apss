INF = 987654321
CACHE = [[]]


def graduate(semester, taken, k, m, classes, n, prerequisite, l):
    global CACHE
    if bin(taken).count("1") >= k:
        return 0
    if semester == m:
        return INF
    if CACHE[semester][taken] != -1:
        return CACHE[semester][taken]
    CACHE[semester][taken] = INF
    can_take = (classes[semester] & ~taken)
    for i in range(n):
        if (can_take & (1 << i)) and \
                (taken & prerequisite[i]) != prerequisite[i]:
            can_take = can_take & ~(1 << i)
    take = can_take
    while take != 0:
        if bin(take).count("1") > l:
            take = (take-1) & can_take
            continue
        CACHE[semester][taken] = min(
            CACHE[semester][taken],
            graduate(semester+1, taken | take,
                     k, m, classes, n, prerequisite, l) + 1
        )
        take = (take-1) & can_take
    CACHE[semester][taken] = min(
        CACHE[semester][taken],
        graduate(semester+1, taken,
                 k, m, classes, n, prerequisite, l)
    )
    return CACHE[semester][taken]


def graduation(input_case):
    global CACHE
    input_list = list(
        map(
            lambda x: [int(i) for i in x.strip().split(' ')],
            input_case.split('\n')
        )
    )
    case_num = int(input_list[0][0])
    input_list = input_list[1:]

    case_start = 0
    for i in range(case_num):
        start = case_start
        n = input_list[start][0]
        k = input_list[start][1]
        m = input_list[start][2]
        max_l = input_list[start][3]
        subjects = input_list[start+1:start+1+n]
        prerequisite = []
        for subject in subjects:
            if subject[0] != 0:
                pre_sum = 0
                for pre in subject[1:]:
                    pre_sum = pre_sum+(1 << pre)
                prerequisite.append(pre_sum)
            else:
                prerequisite.append(0)
        semesters = input_list[start+1+n:start+1+n+m]
        classes = []
        for semester in semesters:
            if semester[0] != 0:
                pre_sum = 0
                for pre in semester[1:]:
                    pre_sum = pre_sum+(1 << pre)
                classes.append(pre_sum)
            else:
                classes.append(0)
        pre_sum = 0
        for z in range(max_l):
            pre_sum = pre_sum + (1 << z)
        CACHE = [
            [-1 for t in range(pre_sum)] for j in range(n)
        ]
        print graduate(1, 0, k, m, classes, n, prerequisite, max_l)
        case_start = start+1+n+m


if __name__ == '__main__':
    input_case = \
        '''2
        4 4 4 4
        0
        1 0
        3 0 1 3
        0
        4 0 1 2 3
        4 0 1 2 3
        3 0 1 3
        4 0 1 2 3
        4 2 2 4
        1 1
        0
        1 3
        1 2
        3 0 2 3
        3 1 2 3'''
    graduation(input_case)
