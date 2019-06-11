def decision(dist, city_num, city_list, target):
    ret = 0
    for i in range(city_num):
        if dist >= (city_list[i][0] - city_list[i][1]):
            ret += (
                (min(dist, city_list[i][0])-(city_list[i][0]-city_list[i][1]))
                / city_list[i][2] + 1
            )
    return ret >= target


def optimize(city_num, city_list, target):
    lo = -1
    hi = 8030001
    while(lo + 1 < hi):
        mid = (lo + hi) / 2
        if decision(mid, city_num, city_list, target):
            hi = mid
        else:
            lo = mid
    return hi


def canadatrip(input_case):
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
        city_num = input_list[start][0]
        target = input_list[start][1]
        city_list = input_list[start+1:start+1+city_num]
        print optimize(city_num, city_list, target)
        case_start = start + 1 + city_num


if __name__ == '__main__':
    input_case = \
        '''2
        3 15
        500 100 10
        504 16 4
        510 60 6
        2 1234567
        8030000 8030000 1
        2 2 1'''
    canadatrip(input_case)
