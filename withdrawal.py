def decision(avg, subject_total_num, subject_remain_num, subject_list):
    v = []
    for i in range(subject_total_num):
        v.append(avg * subject_list[i][1] - subject_list[i][0])
    v.sort()
    ret = 0
    for i in range(subject_total_num-subject_remain_num, subject_total_num):
        ret = ret + v[i]
    return ret >= 0


def optimize(subject_total_num, subject_remain_num, subject_list):
    lo = -1e-9
    hi = 1
    for i in range(100):
        mid = (lo + hi) / 2
        if decision(mid, subject_total_num, subject_remain_num, subject_list):
            hi = mid
        else:
            lo = mid
    return hi


def withdrawal(input_case):
    input_list = list(
        map(
            lambda x: [int(i) for i in x.strip().split(' ')],
            input_case.split('\n')
        )
    )
    case_num = int(input_list[0][0])
    input_list = input_list[1:]
    for i in range(case_num):
        subject_total_num = input_list[i*2][0]
        subject_remain_num = input_list[i*2][1]
        subject_list = []
        for j in range(subject_total_num):
            subject_list.append(input_list[i*2+1][j*2:j*2+2])
        print optimize(subject_total_num, subject_remain_num, subject_list)


if __name__ == '__main__':
    input_case = \
        '''3
        3 2
        1 4 6 10 10 17
        4 2
        4 8 9 12 3 10 2 5
        10 5
        70 180 192 192 1 20 10 200 6 102 60 1000 4 9 1 12 8 127 100 700'''
    withdrawal(input_case)
