def solve(n, k):
    survivors = [i+1 for i in range(n)]
    kill = 0
    while n > 2:
        del survivors[kill]
        if kill == len(survivors):
            kill = 0
        n = n-1
        for i in range(k-1):
            kill = kill+1
            if kill == len(survivors):
                kill = 0
    return survivors


def josephus(input_case):
    global CACHE
    input_list = list(
        map(
            lambda x: [int(i) for i in x.strip().split(' ')],
            input_case.split('\n')
        )
    )
    case_num = int(input_list[0][0])
    input_list = input_list[1:]

    for i in range(case_num):
        n = input_list[i][0]
        k = input_list[i][1]
        print solve(n, k)


if __name__ == '__main__':
    input_case = \
        '''2
        6 3
        40 3'''
    josephus(input_case)
