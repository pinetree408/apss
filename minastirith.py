import math

INF = 987654321


def solver_linear(begin, end, input_range, range_list):
    used = 0
    idx = 0
    while (begin < end):
        max_cover = -1
        while (idx < input_range) and (range_list[idx][0] <= begin):
            max_cover = max(max_cover, range_list[idx][1])
            idx = idx + 1
        if max_cover <= begin:
            return INF
        begin = max_cover
        used = used + 1
    return used


def solver_circular(input_range, range_list):
    ret = INF
    for i in range(input_range):
        if (range_list[i][0] <= 0) or (range_list[i][1] >= 2*math.pi):
            begin = math.fmod(range_list[i][1], 2*math.pi)
            end = math.fmod(range_list[i][0] + 2*math.pi, 2*math.pi)
            ret = min(ret, 1 + solver_linear(
                begin, end, input_range, range_list
            ))
    return ret


def convert_to_range(input_range, input_list):
    range_list = []
    for i in range(input_range):
        loc = math.fmod(
            math.pi*2 +
            math.atan2(
                input_list[i][0],
                input_list[i][1]
            ),
            math.pi*2
        )
        new_range = 2 * math.asin(input_list[i][2] / 2.0 / 8.0)
        range_list.append([loc - new_range, loc + new_range])
    return range_list


def minastrith(input_case):
    input_list = list(
        map(
            lambda x: [float(i) for i in x.strip().split(' ')],
            input_case.split('\n')
        )
    )
    case_num = int(input_list[0][0])
    input_list = input_list[1:]
    cursor = 0
    for i in range(case_num):
        input_range = int(input_list[cursor][0])
        range_list = convert_to_range(
            input_range,
            input_list[cursor+1:cursor+1+input_range]
        )
        range_list.sort(key=lambda x: x[0])
        print solver_circular(
            input_range,
            range_list
        )
        cursor = cursor+1+input_range


if __name__ == '__main__':
    input_case = \
        '''3
        10
        7.02066050 -3.83540431 4.0
        -7.23257714 -3.41903904 2.0
        0.00000000 -8.00000000 8.0
        -8.00000000 -0.00000000 4.8
        -6.47213595 4.70228202 3.2
        -4.70228202 6.47213595 4.8
        7.60845213 -2.47213595 1.6
        -2.47213595 -7.60845213 8.8
        6.47213595 4.70228202 7.6
        -0.00000000 8.00000000 4.8
        4
        8.00000000 0.00000000 8.0
        0.00000000 -8.00000000 8.0
        -8.00000000 0.00000000 8.0
        1.25147572 7.90150672 5.40
        1
        8 0 15.99'''
    minastrith(input_case)
