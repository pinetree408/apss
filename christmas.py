MOD = 20091101


def ways_to_buy(psum, k):
    ret = 0
    count = [0 for i in range(k)]
    for i in range(len(psum)):
        count[psum[i]] = count[psum[i]]+1
    for i in range(k):
        if count[i] >= 2:
            ret = (ret+((count[i]*(count[i]-1))/2)) % MOD
    return ret


def max_buys(psum, k):
    ret = [0 for i in range(len(psum))]
    prev = [-1 for i in range(k)]
    for i in range(len(psum)):
        if i > 0:
            ret[i] = ret[i-1]
        else:
            ret[i] = 0
        loc = prev[psum[i]]
        if loc != -1:
            ret[i] = max(ret[i], ret[loc]+1)
        prev[psum[i]] = i
    return ret[len(ret)-1]


def partial_sum(a, k):
    ret = [0 for i in range(len(a)+1)]
    ret[0] = 0
    for i in range(1, len(a)+1):
        ret[i] = (ret[i-1]+a[i-1]) % k
    return ret


def graduation(input_case):
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
        k = input_list[i*2][1]
        dolls = input_list[i*2+1]
        psum = partial_sum(dolls, k)
        print ways_to_buy(psum, k), max_buys(psum, k)


if __name__ == '__main__':
    input_case = \
        '''2
        6 4
        1 2 3 4 5 6
        4 1
        1 2 3 4'''
    graduation(input_case)
