def solve(n, a):
    arr = [i+1 for i in range(n)]
    for i in range(n-1, 0, -1):
        j = i
        move = a[j]
        if i > 0:
            for k in range(a[j]):
                arr[i-move], arr[i-move+1] = arr[i-move+1], arr[i-move]
                i = i+1
        i = j
    return arr


def insertion(input_case):
    input_list = list(
        map(
            lambda x: [int(i) for i in x.strip().split(' ')],
            input_case.split('\n')
        )
    )
    case_num = int(input_list[0][0])
    input_list = input_list[1:]

    for i in range(case_num):
        n = input_list[i*2][0]
        a = input_list[i*2+1]
        print solve(n, a)


if __name__ == '__main__':
    input_case = \
        '''2
        5
        0 1 1 2 3
        4
        0 1 2 3'''
    insertion(input_case)
