FACTORS = []


def get_factor_brute():
    global FACTORS
    tm = 10*1000*1000
    FACTORS = [0 for i in range(tm+1)]
    for i in range(1, tm+1):
        for j in range(i, tm+1, i):
            FACTORS[j] = FACTORS[j] + 1


def pass486(input_case):
    global FACTORS
    input_list = list(
        map(
            lambda x: [int(i) for i in x.strip().split(' ')],
            input_case.split('\n')
        )
    )
    case_num = int(input_list[0][0])
    input_list = input_list[1:]

    # Get Factros
    get_factor_brute()

    # Start inference
    for i in range(case_num):
        num = input_list[i][0]
        lo = input_list[i][1]
        hi = input_list[i][2]
        count = 0
        for j in range(lo, hi+1):
            if FACTORS[j] == num:
                count = count + 1
        print count


if __name__ == '__main__':
    input_case = \
        '''3
        2 2 10
        12 486 486
        200 1000000 2000000'''
    pass486(input_case)
