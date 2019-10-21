seen = []
order = []


def make_graph(target_list):
    abj = [[0 for i in range(26)] for j in range(26)]
    for j in range(1, len(target_list)):
        i = j-1
        min_len = min(len(target_list[i]), len(target_list[j]))
        for k in range(min_len):
            if target_list[i][k] != target_list[j][k]:
                a = ord(target_list[i][k])-ord('a')
                b = ord(target_list[j][k])-ord('a')
                abj[a][b] = 1
                break
    return abj


def dfs(here, abj):
    global seen, order
    seen[here] = 1
    for there in range(len(abj)):
        if abj[here][there] and not seen[there]:
            dfs(there, abj)
    order.append(here)


def topological_sort(abj):
    global seen, order
    n = len(abj)
    seen = [0 for i in range(n)]
    order = []
    for i in range(n):
        if not seen[i]:
            dfs(i, abj)
    order.reverse()
    for i in range(n):
        for j in range(i+1, n):
            if abj[order[j]][order[i]]:
                return []
    return order


def solve(target_list):
    abj = make_graph(target_list)
    result = topological_sort(abj)
    if len(result) == 0:
        print "INVALID HYPOTHESIS"
    else:
        result_str = ""
        for i in result:
            result_str = result_str+chr(i+ord('a'))
        print result_str


def dictionary(input_case):
    global cache, counter
    input_list = list(
        map(
            lambda x: [i for i in x.strip().split(' ')],
            input_case.split('\n')
        )
    )
    case_num = int(input_list[0][0])
    input_list = input_list[1:]

    start_num = 0
    for i in range(case_num):
        target_num = int(input_list[start_num][0])
        target_list = list(
            map(
                lambda x: x[0],
                input_list[start_num+1:start_num+1+target_num]
            )
        )
        solve(target_list)
        start_num = start_num+1+target_num


if __name__ == '__main__':
    input_case = \
        '''3
        3
        ba
        aa
        ab
        5
        gg
        kia
        lotte
        lg
        hanwha
        6
        dictionary
        english
        is
        ordered
        ordinary
        this'''
    dictionary(input_case)
