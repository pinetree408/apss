CACHE = [[]]


def heat(n, e, m):
    order = []
    for i in range(n):
        order.append([-e[i], i])
    sorted(order, key=lambda x: x[0])
    ret = 0
    begin_eat = 0
    for i in range(n):
        box = order[i][1]
        begin_eat = begin_eat + m[box]
        ret = max(ret, begin_eat + e[box])
    return ret


def lunchbox(input_case):
    global CACHE
    input_list = list(
        map(
            lambda x: [int(i) for i in x.strip().split(' ')],
            input_case.split('\n')
        )
    )
    case_num = int(input_list[0][0])
    input_list = input_list[1:]
    for i in range(case_num):
        test_input = input_list[i*3:3*(i+1)]
        n = test_input[0][0]
        e = test_input[1]
        m = test_input[2]
        print heat(n, e, m)


if __name__ == '__main__':
    input_case = \
        '''2
        3
        2 2 2
        2 2 2
        3
        1 2 3
        1 2 1'''
    lunchbox(input_case)
