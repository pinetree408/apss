graph = [[[] for j in range(26)] for i in range(26)]
adj = [[0 for j in range(26)] for i in range(26)]
indegree = [0 for i in range(26)]
outdegree = [0 for i in range(26)]


def make_graph(word_list):
    global graph, adj, indegree, outdegree
    for i in range(26):
        for j in range(26):
            graph[i][j][:] = []
    adj = [[0 for j in range(26)] for i in range(26)]
    indegree = [0 for i in range(26)]
    outdegree = [0 for i in range(26)]
    for i in range(len(word_list)):
        a = ord(word_list[i][0])-ord('a')
        b = ord(word_list[i][len(word_list[i])-1])-ord('a')
        graph[a][b].append(word_list[i])
        adj[a][b] = adj[a][b] + 1
        outdegree[a] = outdegree[a] + 1
        indegree[b] = indegree[b] + 1


def check_euler():
    global indegree, outdegree
    plus = 0
    minus = 0
    for i in range(26):
        delta = outdegree[i] - indegree[i]
        if delta < -1 or 1 < delta:
            return False
        if delta == 1:
            plus = plus + 1
        if delta == -1:
            minus = minus + 1
    return (
        (plus == 1 and minus == 1) or (plus == 0 and minus == 0)
    )


def get_euler_circuit(here, circuit):
    global adj
    for there in range(len(adj[here])):
        while adj[here][there] > 0:
            adj[here][there] = adj[here][there] - 1
            get_euler_circuit(there, circuit)
    circuit.append(here)


def get_euler_trail_or_circuit():
    global indegree, outdegree
    circuit = []
    for i in range(26):
        if outdegree[i] == indegree[i] + 1:
            get_euler_circuit(i, circuit)
            return circuit
    for i in range(26):
        if outdegree[i]:
            get_euler_circuit(i, circuit)
            return circuit
    return circuit


def solve(word_list):
    global graph
    make_graph(word_list)
    if not check_euler():
        return "IMPOSSIBLE"
    circuit = get_euler_trail_or_circuit()
    if len(circuit) != len(word_list) + 1:
        return "IMPOSSIBLE"
    circuit.reverse()
    ret = ""
    for i in range(1, len(circuit)):
        a = circuit[i-1]
        b = circuit[i]
        if len(ret):
            ret = ret + " "
        ret = ret + graph[a][b].pop()
    return ret


def wordchain(input_case):
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
        print solve(target_list)
        start_num = start_num+1+target_num


if __name__ == '__main__':
    input_case = \
        '''3
        4
        dog
        god
        dragon
        need
        3
        aa
        ab
        bb
        2
        ab
        cd'''
    wordchain(input_case)
