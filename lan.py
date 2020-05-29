import math


class DisJoinSet:
    def __init__(self, n):
        self.parent = [0 for i in range(n)]
        self.rank = [1 for i in range(n)]
        for i in range(n):
            self.parent[i] = i

    def find(self, u):
        if u == self.parent[u]:
            return u
        self.parent[u] = self.find(self.parent[u])
        return self.parent[u]

    def merge(self, u, v):
        u = self.find(u)
        v = self.find(v)
        if u == v:
            return
        if self.rank[u] > self.rank[v]:
            u, v = v, u
        self.parent[u] = v
        if self.rank[u] == self.rank[v]:
            self.rank[v] = self.rank[v] + 1


class Solver:
    def __init__(self):
        self.INF = 987654321

    def kruskal(self, n, point, dis_join_set):
        ret = 0.0
        edge = []
        for i in range(n):
            for j in range(i+1, n):
                sub_x = abs(point[i][0] - point[j][0])
                sub_y = abs(point[i][1] - point[j][1])
                dist = math.sqrt(pow(sub_x, 2) + pow(sub_y, 2))
                edge.append([dist, [i, j]])
        edge.sort()
        for i in range(len(edge)):
            cost = edge[i][0]
            u = edge[i][1][0]
            v = edge[i][1][1]
            if dis_join_set.find(u) == dis_join_set.find(v):
                continue
            dis_join_set.merge(u, v)
            ret = ret+cost
        return ret

    def solve(self, input_case):
        n = int(input_case[0].split(' ')[0])
        m = int(input_case[0].split(' ')[1])
        point = [[0, 0] for i in range(n)]
        lan_set = DisJoinSet(n)
        for i in range(n):
            x = int(input_case[1].split(' ')[i])
            y = int(input_case[2].split(' ')[i])
            point[i][0] = x
            point[i][1] = y
        for i in range(m):
            u = int(input_case[3+i].split(' ')[0])
            v = int(input_case[3+i].split(' ')[1])
            lan_set.merge(u, v)
        ret = self.kruskal(n, point, lan_set)

        return round(ret, 10)


class Tester:
    def __parse_input_cases(self, input_case_list):
        self.T = int(input_case_list[0])
        input_case_list = input_case_list[1:]
        parsed_input_case_list = []
        cursor = 0
        for i in range(self.T):
            m = int(input_case_list[cursor].split(' ')[1])
            parsed_input_case_list.append(
                input_case_list[cursor:cursor+m+2+1]
            )
            cursor = cursor+m+2+1
        return parsed_input_case_list

    def __parse_output_cases(self, output_cases):
        output_case_list = list(
            map(
                lambda x: x.strip(),
                output_cases.split('\n')
            )
        )
        return output_case_list[1:]

    def set_input_cases(self, input_cases):
        input_case_list = list(
            map(
                lambda x: x.strip(),
                input_cases.split('\n')
            )
        )
        self.input_case_list = self.__parse_input_cases(input_case_list)

    def set_output_cases(self, output_cases):
        self.output_case_list = self.__parse_output_cases(output_cases)

    def test_solver(self, solver):
        print("Answer\tResult\tIsCorrect")
        for t in range(self.T):
            result = solver.solve(self.input_case_list[t])
            answer = float(self.output_case_list[t])
            print(str(answer)+"\t"+str(result)+"\t"+str(answer == result))


if __name__ == '__main__':
    '''
    problem link: https://algospot.com/judge/problem/read/LAN
    '''

    input_cases = \
        '''2
        3 1
        0 0 1
        0 1 2
        0 1
        10 5
        -7 -7 10 -4 10 -4 -5 0 -10 -6
        6 8 -5 3 -4 6 -10 4 -7 10
        9 7
        7 3
        9 7
        5 0
        8 6'''

    output_cases = \
        '''2
        1.4142135624
        29.7042202421'''

    tester = Tester()
    solver = Solver()

    tester.set_input_cases(input_cases)
    tester.set_output_cases(output_cases)

    tester.test_solver(solver)
