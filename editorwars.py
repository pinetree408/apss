class BipartiteUnionFind(object):
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.rank = [0 for i in range(n)]
        self.enemy = [-1 for i in range(n)]
        self.size = [1 for i in range(n)]

    def find(self, u):
        if self.parent[u] == u:
            return u
        self.parent[u] = self.find(self.parent[u])
        return self.parent[u]

    def merge(self, u, v):
        if u == -1 or v == -1:
            return max(u, v)
        u = self.find(u)
        v = self.find(v)

        if u == v:
            return u

        if self.rank[u] > self.rank[v]:
            u, v = v, u
        if self.rank[u] == self.rank[v]:
            self.rank[v] = self.rank[v]+1
        self.parent[u] = v
        self.size[v] = self.size[v]+self.size[u]
        return v

    def dis(self, u, v):
        u = self.find(u)
        v = self.find(v)

        if u == v:
            return False

        a = self.merge(u, self.enemy[v])
        b = self.merge(v, self.enemy[u])
        self.enemy[a] = b
        self.enemy[b] = a

        return True

    def ack(self, u, v):
        u = self.find(u)
        v = self.find(v)

        if self.enemy[u] == v:
            return False

        a = self.merge(u, v)
        b = self.merge(self.enemy[u], self.enemy[v])
        self.enemy[a] = b

        if b != -1:
            self.enemy[b] = a

        return True


def max_party(buf, n):
    result = 0
    for node in range(n):
        if buf.parent[node] == node:
            enemy = buf.enemy[node]
            if enemy > node:
                continue
            my_size = buf.size[node]
            enemy_size = 0 if enemy == -1 else buf.size[enemy]
            result = result+max(my_size, enemy_size)
    return result


def editorwars(input_case):
    input_list = list(
        map(
            lambda x: [i for i in x.strip().split(' ')],
            input_case.split('\n')
        )
    )
    case_num = int(input_list[0][0])
    input_list = input_list[1:]

    case_start = 0
    for i in range(case_num):
        start = case_start
        n = int(input_list[start][0])
        m = int(input_list[start][1])
        comments = input_list[start+1:start+1+m]
        comments = list(
            map(
                lambda x: [x[0], int(x[1]), int(x[2])],
                comments
            )
        )
        buf = BipartiteUnionFind(n)
        num = -1
        contradict = False
        for j in range(m):
            if contradict:
                continue
            if comments[j][0] == "ACK":
                if not buf.ack(comments[j][1], comments[j][2]):
                    contradict = True
                    num = i+1
            else:
                if not buf.dis(comments[j][1], comments[j][2]):
                    contradict = True
                    num = i+1
        if contradict:
            print num
        else:
            print max_party(buf, n)
        case_start = start+1+m


if __name__ == '__main__':
    input_case = \
        '''4
        4 4
        ACK 0 1
        ACK 1 2
        DIS 1 3
        ACK 2 0
        100 4
        ACK 0 1
        ACK 1 2
        ACK 2 3
        ACK 3 4
        3 3
        ACK 0 1
        ACK 1 2
        DIS 2 0
        8 6
        DIS 0 1
        ACK 1 2
        ACK 1 4
        DIS 4 3
        DIS 5 6
        ACK 5 7'''
    editorwars(input_case)
