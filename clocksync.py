switch_list = [
    [0, 1, 2],
    [3, 7, 9, 11],
    [4, 10, 14, 15],
    [0, 4, 5, 6, 7],
    [6, 7, 8, 10, 12],
    [0, 2, 14, 15],
    [3, 14, 15],
    [4, 5, 7, 14, 15],
    [1, 2, 3, 4, 5],
    [3, 4, 5, 9, 13],
]
INF = 9999

def is_aligned(clock_list):
    if sum(clock_list) == len(clock_list) * 12:
        return True
    else:
        return False


def push(clock_list, switch_id):
    for clock in switch_list[switch_id]:
        clock_list[clock] += 3
        if clock_list[clock] == 15:
            clock_list[clock] = 3


def solve(clock_list, switch_id):
    if (switch_id == len(switch_list)):
        return 0 if is_aligned(clock_list) else INF
    ret = INF
    for i in range(4):
        ret = min([ret, i + solve(clock_list, switch_id + 1)])
        push(clock_list, switch_id)
    return ret

def clocksync(input_case):
    input_list = list(
        map(
            lambda x: x.strip(),
            input_case.split('\n')
        )
    )
    case_num = int(input_list[0])
    input_list = input_list[1:]
    for i in range(case_num):
        case = input_list[i]
        clock_list = list(map(lambda x: int(x), case.split(' ')))
        print solve(clock_list, 0)


if __name__ == '__main__':
    input_case = \
        '''2
        12 6 6 6 6 6 12 12 12 12 12 12 12 12 12 12
        12 9 3 12 6 6 9 3 12 9 12 9 12 12 6 6'''
    # 2, 9
    clocksync(input_case)
