UPPER = []
LOWER = []


def min_x(hull):
    return min(hull, key=lambda x: x[0])[0]


def max_x(hull):
    return max(hull, key=lambda x: x[0])[0]


def between(a, b, x):
    return (a[0] <= x and x <= b[0]) or (b[0] <= x and x <= a[0])


def at(a, b, x):
    dy = b[1] - a[1]
    dx = b[0] - a[0]
    return a[1] + dy*(x-a[0])/dx


def vertical(x):
    global UPPER, LOWER
    min_up = 1e20
    max_low = -1e20
    for i in range(len(UPPER)):
        if between(UPPER[i][0], UPPER[i][1], x):
            min_up = min(min_up, at(UPPER[i][0], UPPER[i][1], x))
    for i in range(len(LOWER)):
        if between(LOWER[i][0], LOWER[i][1], x):
            max_low = max(max_low, at(LOWER[i][0], LOWER[i][1], x))
    return min_up - max_low


def solve(n_list, m_list):
    lo = max(min_x(n_list), min_x(m_list))
    hi = min(max_x(n_list), max_x(m_list))
    if hi < lo:
        return 0
    for i in range(100):
        aab = (2*lo+hi)/3.0
        abb = (lo+2*hi)/3.0
        if vertical(aab) < vertical(abb):
            lo = aab
        else:
            hi = abb
    return max(0.0, vertical(hi))


def decompose(hull):
    global UPPER, LOWER
    n = len(hull)
    for i in range(n):
        if hull[i][0] < hull[(i+1) % n][0]:
            LOWER.append([hull[i], hull[(i+1) % n]])
        elif hull[i][0] > hull[(i+1) % n][0]:
            UPPER.append([hull[i], hull[(i+1) % n]])


def fossil(input_case):
    input_list = list(
        map(
            lambda x: [float(i) for i in x.strip().split(' ')],
            input_case.split('\n')
        )
    )
    case_num = int(input_list[0][0])
    input_list = input_list[1:]
    for i in range(case_num):
        n = int(input_list[i*3][0])
        m = int(input_list[i*3][1])
        n_list = []
        for n_i in range(n):
            n_list.append(input_list[i*3+1][n_i*2:n_i*2+2])
        m_list = []
        for m_i in range(m):
            m_list.append(input_list[i*3+2][m_i*2:m_i*2+2])
        decompose(n_list)
        decompose(m_list)
        print solve(n_list, m_list)


if __name__ == '__main__':
    input_case = \
        '''2
        5 5
        35.74 35.85 69.64 50.00 73.52 82.55 43.50 92.22 17.67 76.18
        16.47 8.02 60.98 14.62 66.80 37.74 45.89 67.22 13.04 55.19
        4 3
        73.84 11.41 71.61 32.72 39.87 38.84 22.41 17.87
        75.13 51.64 47.72 87.34 15.97 64.56'''
    fossil(input_case)
