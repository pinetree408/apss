adj = [[]]
visited = []
installed = 0
UNWATCHED = 0
WATCHED = 1
INSTALLED = 2


def dfs(here):
    global visited, adj, installed
    visited[here] = True
    children = [0, 0, 0]
    for i in range(len(adj[here])):
        there = adj[here][i]
        if not visited[there]:
            children[dfs(there)] += 1
    if children[UNWATCHED]:
        installed += 1
        return INSTALLED
    if children[INSTALLED]:
        return WATCHED
    return UNWATCHED


def solve():
    global adj, visited, installed
    installed = 0
    visited = [False for i in range(len(adj))]
    for i in range(len(visited)):
        if (not visited[i]) and dfs(i) == UNWATCHED:
            installed += 1
    return installed


def gallery(input_case):
    global adj
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
        target_num = int(input_list[start_num][1])
        target_list = list(
            map(
                lambda x: [int(x[0]), int(x[1])],
                input_list[start_num+1:start_num+1+target_num]
            )
        )
        adj = [[] for j in range(int(input_list[start_num][0]))]
        for k in range(target_num):
            u = target_list[k][0]
            v = target_list[k][1]
            adj[u].append(v)
            adj[v].append(u)
        print solve()
        start_num = start_num+1+target_num


if __name__ == '__main__':
    input_case = \
        '''3
        6 5
        0 1
        1 2
        1 3
        2 5
        0 4
        4 2
        0 1
        2 3
        1000 1
        0 1'''
    gallery(input_case)
