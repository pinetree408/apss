def get_partial_match(N):
    m = len(N)
    pi = [0 for i in range(m)]
    begin = 1
    matched = 0
    while begin+matched < m:
        if N[begin+matched] == N[matched]:
            matched = matched+1
            pi[begin+matched-1] = matched
        else:
            if matched == 0:
                begin = begin+1
            else:
                begin = begin+matched-pi[matched-1]
                matched = pi[matched-1]
    return pi


def kmp_search(H, N):
    n = len(H)
    m = len(N)
    ret = []
    pi = get_partial_match(N)

    matched = 0
    for i in range(n):
        while ((matched > 0) and (H[i] != N[matched])):
            matched = pi[matched-1]
        if H[i] == N[matched]:
            matched = matched+1
            if matched == m:
                ret.append(i-m+1)
                matched = pi[matched-1]
    return ret


def solve(safe_list):
    result = 0
    for i in range(len(safe_list)-1):
        if i % 2 == 0:
            result = result+kmp_search(
                safe_list[i+1][0]*2,
                safe_list[i][0]
            )[0]
        else:
            result = result+kmp_search(
                safe_list[i][0]*2,
                safe_list[i+1][0]
            )[0]
    return result


def ites(input_case):
    global last_signal
    input_list = list(
        map(
            lambda x: [str(i) for i in x.strip().split(' ')],
            input_case.split('\n')
        )
    )
    case_num = int(input_list[0][0])
    input_list = input_list[1:]

    case_start = 0
    for i in range(case_num):
        start = case_start
        n = int(input_list[start][0])
        safe_list = input_list[start+1:start+1+n+1]
        print solve(safe_list)
        case_start = start+1+n+1


if __name__ == '__main__':
    input_case = \
        '''2
        3
        abbab
        babab
        ababb
        bbaba
        2
        RMDCMRCD
        MRCDRMDC
        DCMRCDRM'''
    ites(input_case)
