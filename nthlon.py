class Solver:
    def __init__(self):
        self.INF = 987654321

    def dijkstra(self, adj):
        bucket = [self.INF for i in range(400)]
        pq = []

        bucket[0] = 0
        pq.append([0, 0])

        while len(pq) != 0:
            item = pq.pop()
            here = item[1]
            cost = -item[0]

            if cost > bucket[here]:
                continue

            for i in range(len(adj[here])):
                there = adj[here][i][0]
                c = adj[here][i][1]
                if c+cost < bucket[there]:
                    bucket[there] = c+cost
                    pq.append([-(c+cost), there])
        ret = bucket[200]
        if ret == self.INF:
            ret = "IMPOSSIBLE"
        return str(ret)

    def solve(self, input_case):
        adj = [[] for i in range(400)]
        for i in range(len(input_case)):
            x = int(input_case[i].split()[0])
            y = int(input_case[i].split()[1])
            gap = x-y
            for j in range(400):
                if j+gap < 1 or j+gap >= 400:
                    continue
                adj[j].append([j+gap, x])
            adj[0].append([200+gap, x])

        return self.dijkstra(adj)


class Tester:
    def __parse_input_cases(self, input_cases):
        input_case_list = list(
            map(
                lambda x: x.strip(),
                input_cases.split('\n')
            )
        )
        self.T = int(input_case_list[0])
        input_case_list = input_case_list[1:]
        parsed_input_case_list = []
        cursor = 0
        for i in range(self.T):
            num = int(input_case_list[cursor])
            parsed_input_case_list.append(
                input_case_list[cursor+1:cursor+num+1]
            )
            cursor = cursor+num+1
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
        self.input_case_list = self.__parse_input_cases(input_cases)

    def set_output_cases(self, output_cases):
        self.output_case_list = self.__parse_output_cases(output_cases)

    def test_solver(self, solver):
        print("Answer\tResult\tIsCorrect")
        for t in range(self.T):
            result = solver.solve(self.input_case_list[t])
            answer = self.output_case_list[t]
            print(str(answer)+"\t"+str(result)+"\t"+str(answer == result))


if __name__ == '__main__':
    '''
    problem link: https://algospot.com/judge/problem/read/NTHLON
    '''

    input_cases = \
        '''3
        5
        1 2
        3 4
        5 6
        7 8
        7 3
        3
        1 100
        21 20
        10 1 
        3
        10 81
        63 71
        16 51'''

    output_cases = \
        '''3
        11
        111
        IMPOSSIBLE'''

    tester = Tester()
    solver = Solver()

    tester.set_input_cases(input_cases)
    tester.set_output_cases(output_cases)

    tester.test_solver(solver)
