import copy


class Solver:
    def __init__(self):
        self.INF = 987654321

    def set_default(self, default):
        self.v = int(default[0].split(' ')[0])
        self.e = int(default[0].split(' ')[1])
        self.drunken_cost = []
        for i in range(self.v):
            self.drunken_cost.append(int(default[1].split(' ')[i]))
        self.adj = [[self.INF for i in range(self.v)] for j in range(self.v)]
        for i in range(self.v):
            self.adj[i][i] = 0
        for i in range(self.e):
            a = int(default[2+i].split(' ')[0]) - 1
            b = int(default[2+i].split(' ')[1]) - 1
            c = int(default[2+i].split(' ')[2])
            self.adj[a][b] = c
            self.adj[b][a] = c

    def floyd(self):
        ans = copy.deepcopy(self.adj)
        dist = copy.deepcopy(self.adj)
        order = []
        for i in range(self.v):
            order.append([self.drunken_cost[i], i])
        order.sort()
        for i in range(self.v):
            w = order[i][1]
            for j in range(self.v):
                for k in range(self.v):
                    dist[j][k] = min(dist[j][k], dist[j][w] + dist[w][k])
                    ans[j][k] = min(
                        ans[j][k],
                        dist[j][w] + self.drunken_cost[w] + dist[w][k]
                    )
        return ans

    def solve(self, input_case):
        ans = self.floyd()
        s = int(input_case.split(' ')[0]) - 1
        t = int(input_case.split(' ')[1]) - 1
        return ans[s][t]


class Tester:
    def __parse_input_cases(self, input_case_list):
        self.T = int(input_case_list[0])
        input_case_list = input_case_list[1:]
        parsed_input_case_list = []
        for i in range(self.T):
            parsed_input_case_list.append(input_case_list[i])
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
        e = int(input_case_list[0].split(' ')[1])
        self.default = input_case_list[:1+e+1]
        self.input_case_list = self.__parse_input_cases(
            input_case_list[1+e+1:]
        )

    def set_output_cases(self, output_cases):
        self.output_case_list = self.__parse_output_cases(output_cases)

    def test_solver(self, solver):
        print("Answer\tResult\tIsCorrect")
        for t in range(self.T):
            solver.set_default(self.default)
            result = solver.solve(self.input_case_list[t])
            answer = int(self.output_case_list[t])
            print(str(answer)+"\t"+str(result)+"\t"+str(answer == result))


if __name__ == '__main__':
    '''
    problem link: https://www.algospot.com/judge/problem/read/DRUNKEN
    '''

    input_cases = \
        '''8 12
        8 6 5 8 3 5 8 4
        1 6 9
        1 2 3
        2 8 3
        6 8 5
        6 7 3
        8 7 3
        6 5 5
        4 5 7
        3 4 4
        3 5 2
        2 3 6
        7 5 1
        2
        1 5
        6 3'''

    output_cases = \
        '''2
        17
        10'''

    tester = Tester()
    solver = Solver()

    tester.set_input_cases(input_cases)
    tester.set_output_cases(output_cases)

    tester.test_solver(solver)
