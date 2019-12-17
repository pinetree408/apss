def get_value_from_list(target_key, key_value_list):
    for key_value in key_value_list:
        key = key_value[0]
        value = key_value[1]
        same_flag = False
        for i in range(len(target_key)):
            if target_key[i] != key[i]:
                break
            else:
                if i == len(target_key)-1:
                    same_flag = True
        if same_flag:
            return value
    return -1


def bfs(target):
    n = len(target)
    fixed = [0 for i in range(n)]
    for i in range(n):
        smaller = 0
        for j in range(n):
            if target[j] < target[i]:
                smaller = smaller + 1
        fixed[i] = smaller

    to_sort = []
    perm = [i for i in range(n)]
    q = []
    q.append(perm[:])
    to_sort.append([perm[:], 0])
    while len(q) != 0:
        if get_value_from_list(fixed, to_sort) != -1:
            return get_value_from_list(fixed, to_sort)
        here = q.pop(0)
        cost = get_value_from_list(here, to_sort)
        for i in range(n):
            for j in range(i+2, n+1):
                here[i:j] = here[i:j][::-1]
                if get_value_from_list(here, to_sort) == -1:
                    to_sort.append([here[:], cost+1])
                    q.append(here[:])
                here[i:j] = here[i:j][::-1]
    return -1


def sortgame(input_case):
    input_list = list(
        map(
            lambda x: [i for i in x.strip().split(' ')],
            input_case.split('\n')
        )
    )
    case_num = int(input_list[0][0])
    input_list = input_list[1:]

    for i in range(case_num):
        target_list = list(
            map(
                lambda x: int(x), input_list[2*i+1]
            )
        )
        result = bfs(target_list)
        print(result)


if __name__ == '__main__':
    input_case = \
        '''3
        8
        1 2 3 4 8 7 6 5
        4
        3 4 1 2
        3
        1 2 3'''

    sortgame(input_case)
