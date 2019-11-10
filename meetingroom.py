adj = [[]]
scc_id = []
discovered = []
scc_counter = 0
vertex_counter = 0
st = []


def scc(here):
    global adj, discovered, vertex_counter, scc_id, scc_counter
    ret = vertex_counter
    discovered[here] = vertex_counter
    vertex_counter = vertex_counter + 1
    st.append(here)
    for i in range(len(adj[here])):
        there = adj[here][i]
        if discovered[there] == -1:
            ret = min(ret, scc(there))
        elif scc_id[there] == -1:
            ret = min(ret, discovered[there])
    if ret == discovered[here]:
        while True:
            t = st.pop()
            scc_id[t] = scc_counter
            if t == here:
                break
        scc_counter = scc_counter + 1
    return ret


def tarjan_scc():
    global adj, scc_id, discovered, scc_counter, vertex_counter
    scc_id = [-1 for i in range(len(adj))]
    discovered = [-1 for i in range(len(adj))]
    scc_counter = 0
    vertex_counter = 0
    for i in range(len(adj)):
        if discovered[i] == -1:
            scc(i)
    return scc_id


def solve_sat():
    global adj
    n = len(adj)/2
    label = tarjan_scc()
    for i in range(0, 2*n, 2):
        if label[i] == label[i+1]:
            return []
    value = [-1 for i in range(2*n)]
    order = []
    for i in range(2*n):
        order.append([-label[i], i])
    order.sort()
    for i in range(2*n):
        vertex = order[i][1]
        variable = vertex/2
        is_true = vertex % 2 == 0
        if value[variable] != -1:
            continue
        value[variable] = not is_true
    return value


def disjoint(a, b):
    return (a[1] <= b[0]) or (b[1] <= a[0])


def make_graph(meetings):
    global adj
    adj = [[] for i in range(len(meetings)*2)]
    for i in range(0, len(meetings), 2):
        j = i+1
        adj[i*2+1].append(j*2)
        adj[j*2+1].append(i*2)
    for i in range(len(meetings)):
        for j in range(i):
            if not disjoint(meetings[i], meetings[j]):
                adj[i*2].append(j*2+1)
                adj[j*2].append(i*2+1)


def solve(meetings):
    make_graph(meetings)
    ans = solve_sat()
    if len(ans) > 0:
        print "POSSIBLE"
        for i in range(0, len(meetings), 2):
            if ans[i] == 1:
                print (meetings[i][0], meetings[i][1])
            else:
                print (meetings[i+1][0], meetings[i+1][1])
    else:
        print "IMPOSSIBLE"


def meetingroom(input_case):
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
                lambda x: [[int(x[0]), int(x[1])], [int(x[2]), int(x[3])]],
                input_list[start_num+1:start_num+1+target_num]
            )
        )
        meetings = []
        for target in target_list:
            meetings = meetings + target
        solve(meetings)
        start_num = start_num+1+target_num


if __name__ == '__main__':
    input_case = \
        '''3
        2
        1 10 10 20
        1 10 10 20
        3
        1 10 10 20
        1 10 10 20
        1 10 10 20
        3
        2 5 6 9
        1 3 8 10
        4 7 11 12'''
    meetingroom(input_case)
