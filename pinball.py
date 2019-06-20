import math


EPSILON = 1e-9
INFTY = 1e200


def solve(a, b, c):
    d = b*b-4*a*c

    if d < -EPSILON:
        return []
    if d < EPSILON:
        return [1, -b/(2*a)]
    ret = []
    ret.append((-b-math.sqrt(d))/(2*a))
    ret.append((-b+math.sqrt(d))/(2*a))
    return ret


def hit_circle(here, direct, center, radius):
    a = direct[0]*direct[0]+direct[1]*direct[1]
    b = 2*(direct[0]*(here[0]-center[0])+direct[1]*(here[1]-center[1]))
    c = (center[0]*center[0]+center[1]*center[1]) +\
        (here[0]*here[0]+here[1]*here[1]) +\
        -2*(here[0]*center[0]+here[1]*center[1]) +\
        -radius*radius
    sol = solve(a, b, c)
    if len(sol) == 0 or sol[0] < EPSILON:
        return INFTY
    return sol[0]


def reflect(direct, center, contact):
    temp = [contact[0]-center[0], contact[1]-center[1]]
    temp = norm(temp)
    temp_project = (temp[0]*direct[0]+temp[1]*direct[1])
    temp[0] = temp[0]*temp_project
    temp[1] = temp[1]*temp_project
    direct[0] = direct[0]-temp[0]*2
    direct[1] = direct[1]-temp[1]*2
    direct = norm(direct)
    return direct


def norm(vector):
    norm = math.sqrt(vector[0]*vector[0]+vector[1]*vector[1])
    return [vector[0]/norm, vector[1]/norm]


def simulate(here, direct, circle_list):
    direct = norm(direct)
    hit = 0
    while hit < 10:
        circle = -1
        time = INFTY*0.5
        for i in range(len(circle_list)):
            cand = hit_circle(
                here, direct, circle_list[i][:2], circle_list[i][2]+1
            )
            if cand < time:
                time = cand
                circle = i
        if circle == -1:
            break
        print circle
        hit = hit + 1
        contact = [here[0]+direct[0]*time, here[1]+direct[1]*time]
        direct = reflect(direct, circle_list[circle][:2], contact)
        here = contact


def pinball(input_case):
    input_list = list(
        map(
            lambda x: [int(i) for i in x.strip().split(' ')],
            input_case.split('\n')
        )
    )
    case_num = int(input_list[0][0])
    input_list = input_list[1:]

    for i in range(case_num):
        ball = input_list[i][:4]
        obstacle_list = input_list[i+1:i+1+input_list[i][4]]
        simulate(ball[:2], ball[2:4], obstacle_list)


if __name__ == '__main__':
    input_case = \
        '''1
        5 5 1 1 5
        22 40 12
        61 26 20
        19 78 21
        51 86 7
        84 57 15'''
    pinball(input_case)
