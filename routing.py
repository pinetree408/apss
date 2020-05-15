class Solver:
    def dijkstra(self, V, adj):
        dist = [0.0 for i in range(V)]
        dist[0] = 1.0
        pq = [[-1.0, 0]]

        while len(pq) != 0:
            top = pq.pop()
            cost = -top[0]
            here = top[1]

            if dist[here] < cost:
                continue

            for i in range(len(adj[here])):
                there = adj[here][i][0]
                there_dist = cost * adj[here][i][1]

                if dist[there] == 0.0 or dist[there] > there_dist:
                    dist[there] = there_dist
                    pq.append([-dist[there], there])

        return dist[V-1]

    def solve(self, input_case):
        V = int(input_case[0].split()[0])
        E = int(input_case[0].split()[1])

        adj = [[] for i in range(V)]
        for i in range(E):
            if i == E:
                break
            a = int(input_case[i+1].split()[0])
            b = int(input_case[i+1].split()[1])
            c = float(input_case[i+1].split()[2])
            adj[a].append([b, c])
            adj[b].append([a, c])
        ret = self.dijkstra(V, adj)

        return ret


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
            datas = input_case_list[i].split(' ')
            M = int(datas[1])
            parsed_input_case_list.append(input_case_list[cursor:cursor+M+1])
            cursor = cursor+M+1
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
            answer = float(self.output_case_list[t])
            print(str(answer)+"\t"+str(result)+"\t"+str(answer == result))


if __name__ == '__main__':
    '''
    problem link: https://algospot.com/judge/problem/read/ROUTING
    '''

    input_cases = \
        '''1
        7 14
        0 1 1.3
        0 2 1.1
        0 3 1.24
        3 4 1.17
        3 5 1.24
        3 1 2
        1 2 1.31
        1 2 1.26
        1 4 1.11
        1 5 1.37
        5 4 1.24
        4 6 1.77
        5 6 1.11
        2 6 1.2'''

    output_cases = \
        '''1
        1.32'''

    tester = Tester()
    solver = Solver()

    tester.set_input_cases(input_cases)
    tester.set_output_cases(output_cases)

    tester.test_solver(solver)
