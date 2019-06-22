import math


def ccw(p, a, b):
    temp_one = [a[0]-p[0], a[1]-p[1]]
    temp_two = [b[0]-p[0], b[1]-p[1]]
    return temp_one[0]*temp_two[1]-temp_one[1]*temp_two[0]


def norm(vector):
    norm = math.sqrt(vector[0]*vector[0]+vector[1]*vector[1])
    return norm


def gift_wrap(points):
    n = len(points)
    hull = []
    pivots = sorted(points, key=lambda x: x[0])
    pivots = sorted(pivots, key=lambda x: x[1])
    pivot = pivots[0]
    hull.append(pivot)
    while True:
        ph = hull[len(hull)-1]
        next_point = points[0]
        for i in range(n):
            cross = ccw(ph, next_point, points[i])
            dist = norm([next_point[0]-ph[0], next_point[1]-ph[1]]) -\
                norm([points[i][0]-ph[0], points[i][1]-ph[1]])
            if cross > 0 or (cross == 0 and dist < 0):
                next_point = points[i]
        if next_point == pivot:
            break
        hull.append(next_point)
    return hull


def is_inside(q, p):
    crosses = 0
    for i in range(len(p)):
        j = (i+1) % len(p)
        if (p[i][1] > q[1]) != (p[j][1] > q[1]):
            x = (p[j][0]-p[i][0])*(q[1]-p[i][1])/(p[j][1]-p[i][1])+p[i][0]
            if q[0] < x:
                crosses = crosses + 1
    return crosses % 2 > 0


def segment_intersects(a, b, c, d):
    ab = ccw(a, b, c)*ccw(a, b, d)
    cd = ccw(c, d, a)*ccw(c, d, b)
    if ab == 0 and cd == 0:
        if b < a:
            a, b = b, a
        if d < c:
            c, d = d, c
        return not (b < c or d < a)
    return ab <= 0 and cd <= 0


def polygon_intersects(p, q):
    n = len(p)
    m = len(q)
    if is_inside(p[0], q) or is_inside(q[0], p):
        return True
    for i in range(n):
        for j in range(m):
            if segment_intersects(p[i], p[(i+1) % n], q[j], q[(j+1) % m]):
                return True
    return False


def nerd(input_case):
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
        people_num = int(input_list[start][0])
        people_list = input_list[start+1:start+1+people_num]
        nerds = []
        not_nerds = []
        for people in people_list:
            if people[0] == 1:
                nerds.append([people[1], people[2]])
            else:
                not_nerds.append([people[1], people[2]])
        p = gift_wrap(nerds)
        q = gift_wrap(not_nerds)
        print polygon_intersects(p, q)
        case_start = start+1+people_num


if __name__ == '__main__':
    input_case = \
        '''3
        8
        1 2 3
        1 3 4
        1 4 5
        1 2 5
        0 4 1
        0 5 5
        0 3 3
        0 4 4
        6
        1 1 5
        1 5 1
        1 1 1
        0 2 2
        0 4 1
        0 1 4
        6
        1 10 10
        0 10 10
        1 5 15
        1 5 5
        0 15 15
        0 15 5'''
    nerd(input_case)
