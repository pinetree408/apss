import Queue

last_signal = 1983


def solve(k, n):
    q = Queue.Queue()
    ret = 0
    range_sum = 0
    for i in range(n):
        new_signal = signal()
        range_sum = range_sum+new_signal
        q.put(new_signal)

        while range_sum > k:
            range_sum = range_sum-q.get()

        if range_sum == k:
            ret = ret+1
    return ret


def signal():
    global last_signal
    ret = (last_signal % 10000) + 1
    last_signal = (last_signal*214013+2531011) % pow(2, 32)
    return ret


def ites(input_case):
    global last_signal
    input_list = list(
        map(
            lambda x: [int(i) for i in x.strip().split(' ')],
            input_case.split('\n')
        )
    )
    case_num = int(input_list[0][0])
    input_list = input_list[1:]

    for i in range(case_num):
        n = input_list[i][1]
        k = input_list[i][0]
        last_signal = 1983
        print solve(k, n)


if __name__ == '__main__':
    input_case = \
        '''3
        8791 20
        5265 5000
        3578452 5000000'''
    ites(input_case)
