def merge_list(a_idx, b_idx, a_list, b_list):
    if a_idx == -1:
        a = -1
    else:
        a = a_list[a_idx]
    if b_idx == -1:
        b = -1
    else:
        b = b_list[b_idx]

    ret = 2
    max_item = max(a, b)

    for i in range(a_idx+1, len(a_list)):
        if max_item < a_list[i]:
            ret = max(ret, merge_list(i, b_idx, a_list, b_list) + 1)
    for i in range(b_idx+1, len(b_list)):
        if max_item < b_list[i]:
            ret = max(ret, merge_list(a_idx, i, a_list, b_list) + 1)
    return ret


def jlis(input_case):
    input_list = list(
        map(
            lambda x: x.strip(),
            input_case.split('\n')
        )
    )
    case_num = int(input_list[0])
    input_list = input_list[1:]
    for i in range(case_num):
        a_list = list(map(lambda x: int(x), input_list[i*3+1].split(' ')))
        b_list = list(map(lambda x: int(x), input_list[i*3+2].split(' ')))
        print a_list, b_list
        print merge_list(-1, -1, a_list, b_list) - 2


if __name__ == '__main__':
    input_case = \
        '''3
        3 3
        1 2 4
        3 4 7
        3 3
        1 2 3
        4 5 6
        5 3
        10 20 30 1 2
        10 20 30'''
    jlis(input_case)
