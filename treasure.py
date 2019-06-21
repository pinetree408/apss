import math


EPSILON = 1e-9


def ccw(p, a, b):
    temp_one = [a[0]-p[0], a[1]-p[1]]
    temp_two = [b[0]-p[0], b[1]-p[1]]
    return temp_one[0]*temp_two[1]-temp_one[1]*temp_two[0]


def line_intersection(a, b, c, d, x):
    temp_one = [b[0]-a[0], b[1]-a[1]]
    temp_two = [d[0]-c[0], d[1]-c[1]]
    det = temp_one[0]*temp_two[1]-temp_one[1]*temp_two[0]
    if math.fabs(det) < EPSILON:
        return [False, x]
    x_one = [c[0]-a[0], c[1]-a[1]]
    x_two = [d[0]-c[0], d[1]-c[1]]
    x_three = x_one[0]*x_two[1]-x_one[1]*x_two[0]
    x_four = x_three/det
    x_five = [b[0]-a[0], b[1]-a[1]]
    x_six = [x_five[0]*x_four, x_five[1]*x_four]
    x = [a[0]+x_six[0], a[1]+x_six[1]]
    return [True, x]


def cut_poly(p, a, b):
    n = len(p)
    inside = [False for i in range(n)]
    for i in range(n):
        inside[i] = (ccw(a, b, p[i]) >= 0)
    ret = []
    for i in range(n):
        j = (i+1) % n
        if inside[i]:
            ret.append(p[i])
        if inside[i] != inside[j]:
            result = line_intersection(p[i], p[j], a, b, [])
            if result[0]:
                ret.append(result[1])
            else:
                assert result[0]
    return ret


def intersection(p, target):
    a = target[0]
    b = target[1]
    c = target[2]
    d = target[3]
    ret = cut_poly(p, [a, b], [c, b])
    ret = cut_poly(ret, [c, b], [c, d])
    ret = cut_poly(ret, [c, d], [a, d])
    ret = cut_poly(ret, [a, d], [a, b])
    return ret


def area(p):
    ret = 0
    for i in range(len(p)):
        j = (i+1) % len(p)
        ret = ret + (p[i][0]*p[j][1]-p[j][0]*p[i][1])
    return math.fabs(ret)/2.0


def treasure(input_case):
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
        target = input_list[start][:4]
        map_num = int(input_list[start][4])
        map_list = input_list[start+1:start+1+map_num]
        p = intersection(map_list, target)
        print area(p)
        case_start = start+1+map_num


if __name__ == '__main__':
    input_case = \
        '''2
        26 34 76 72 15
        41 52
        50 71
        42 87
        26 84
        16 58
        33 33
        51 23
        64 32
        73 17
        86 14
        91 38
        92 68
        82 79
        68 45
        61 58
        50 20 70 80 4
        86 50
        30 10
        90 50
        30 90'''
    treasure(input_case)
