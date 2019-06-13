MAX_NUM = 2000000000


def _ratio(a, b):
    return (b * 100) / a


def need_games(games, won):
    global MAX_NUM
    if _ratio(games, won) == _ratio(games + MAX_NUM, won + MAX_NUM):
        return -1
    lo = 0
    hi = MAX_NUM

    while lo + 1 < hi:
        mid = (lo + hi) / 2
        if _ratio(games, won) == _ratio(games + mid, won + mid):
            lo = mid
        else:
            hi = mid
    return hi


def ratio(input_case):
    input_list = list(
        map(
            lambda x: [int(i) for i in x.strip().split(' ')],
            input_case.split('\n')
        )
    )
    case_num = int(input_list[0][0])
    input_list = input_list[1:]
    for i in range(case_num):
        total_num = input_list[i][0]
        win_num = input_list[i][1]
        print need_games(total_num, win_num)


if __name__ == '__main__':
    input_case = \
        '''5
        10 8
        100 80
        47 47
        99000 0
        1000000000 470000000'''
    ratio(input_case)
