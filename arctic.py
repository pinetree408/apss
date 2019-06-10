import math


DIST = [[]]


def optimize(base_num):
    low = 0.0
    high = 1416.0
    for i in range(100):
        mid = (low + high) / 2
        if decision(base_num, mid):
            high = mid
        else:
            low = mid
    return high


def decision(base_num, d):
    global DIST
    visited = [False for i in range(base_num)]
    visited[0] = True
    q = []
    q.append(0)
    seen = 0
    while (len(q) != 0):
        here = q.pop(0)
        seen = seen + 1
        for there in range(base_num):
            if (not visited[there]) and DIST[here][there] <= d:
                visited[there] = True
                q.append(there)
    return seen == base_num


def arctic(input_case):
    global DIST
    input_list = list(
        map(
            lambda x: [float(i) for i in x.strip().split(' ')],
            input_case.split('\n')
        )
    )
    case_num = int(input_list[0][0])
    input_list = input_list[1:]
    case_start = 0
    for i in range(case_num):
        start = case_start
        base_num = int(input_list[start][0])
        base_list = input_list[start+1:start+1+base_num]
        DIST = [[0.0 for j in range(base_num)] for i in range(base_num)]
        for i in range(base_num):
            for j in range(base_num):
                source = base_list[i]
                target = base_list[j]
                dist = math.sqrt(
                    math.pow(source[0] - target[0], 2) +
                    math.pow(source[1] - target[1], 2)
                )
                DIST[i][j] = dist
        print optimize(base_num)
        case_start = start + 1 + base_num


if __name__ == '__main__':
    input_case = \
        '''2
        5
        0 0
        1 0
        1 1
        1 2
        0 2
        6
        1.0 1.0
        30.91 8
        4.0 7.64
        21.12 6.0
        11.39 3.0
        5.31 11.0'''
    arctic(input_case)
