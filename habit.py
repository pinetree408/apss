def sort_using_t(perm, group, t):
    for i in range(len(perm)):
        for j in range(i+1, len(perm)):
            if group[perm[i]] != group[perm[j]]:
                if not (group[perm[i]] < group[perm[j]]):
                    perm[i], perm[j] = perm[j], perm[i]
            else:
                if not (group[perm[i]+t] < group[perm[j]+t]):
                    perm[i], perm[j] = perm[j], perm[i]
    return perm


def comparator_using_t(group, t, a, b):
    if group[a] != group[b]:
        return group[a] < group[b]
    else:
        return group[a+t] < group[b+t]


def get_suffix_array(s):
    n = len(s)
    t = 1
    group = [0 for i in range(n+1)]
    for i in range(n):
        group[i] = ord(s[i])
    group[n] = -1
    perm = [0 for i in range(n)]
    for i in range(n):
        perm[i] = i
    while t < n:
        perm = sort_using_t(perm, group, t)
        prev_t = t
        t = t*2
        if t >= n:
            break
        new_group = [0 for i in range(n+1)]
        new_group[n] = -1
        new_group[perm[0]] = 0
        for i in range(1, n):
            if comparator_using_t(group, prev_t, perm[i-1], perm[i]):
                new_group[perm[i]] = new_group[perm[i-1]]+1
            else:
                new_group[perm[i]] = new_group[perm[i-1]]
        group = new_group
    return perm


def common_prefix(s, i, j):
    k = 0
    while (i < len(s)) and (j < len(s)) and s[i] == s[j]:
        i = i+1
        j = j+1
        k = k+1
    return k


def longest_frequent(k, s):
    a = get_suffix_array(s)
    ret = 0
    for i in range(len(s)+1-k):
        ret = max(ret, common_prefix(s, a[i], a[i+k-1]))
    return ret


def habit(input_case):
    input_list = list(
        map(
            lambda x: [str(i) for i in x.strip().split(' ')],
            input_case.split('\n')
        )
    )
    case_num = int(input_list[0][0])
    input_list = input_list[1:]

    for i in range(case_num):
        k = int(input_list[i*2][0])
        script = input_list[i*2+1][0]
        print longest_frequent(k, script)


if __name__ == '__main__':
    input_case = \
        '''4
        2
        uhmhellouhmmynameislibe
        3
        banana
        1
        thatsagoodquestion
        3
        hello'''
    habit(input_case)
