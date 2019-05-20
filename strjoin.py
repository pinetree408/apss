import heapq


def _strjoin(targets):
    pq = []
    for target in targets:
        heapq.heappush(pq, (target, target))
    ret = 0
    while len(pq) > 1:
        min1 = heapq.heappop(pq)
        min2 = heapq.heappop(pq)
        next_target = min1[0] + min2[0]
        heapq.heappush(pq, (next_target, next_target))
        ret += next_target
    return ret


def strjoin(input_case):
    input_list = list(
        map(
            lambda x: [int(i) for i in x.strip().split(' ')],
            input_case.split('\n')
        )
    )
    case_num = input_list[0][0]
    input_list = input_list[1:]
    for i in range(case_num):
        targets = input_list[(i*2) + 1]
        print _strjoin(targets)


if __name__ == '__main__':
    input_case = \
        '''3
        3
        2 2 4
        5
        3 1 3 4 1
        8
        1 1 1 1 1 1 1 2'''
    strjoin(input_case)
