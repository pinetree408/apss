class Solver:
    def __init__(self):
        self.INF = 987654321

    def dijkstra(self, V, adj, x):
        dist = [self.INF for i in range(V+1)]
        visited = [False for i in range(V+1)]
        dist[x] = 0
        visited[x] = 0

        while True:
            closest = self.INF
            here = -1
            for i in range(V+1):
                if not visited[i] and dist[i] < closest:
                    closest = dist[i]
                    here = i

            if closest == self.INF:
                break

            visited[here] = True
            for i in range(len(adj[here])):
                there = adj[here][i][0]
                if visited[there]:
                    continue

                next_dist = dist[here] + adj[here][i][1]
                dist[there] = min(dist[there], next_dist)

        return dist

    def solve(self, input_case):
        V = int(input_case[0].split()[0])
        E = int(input_case[0].split()[1])
        n = int(input_case[0].split()[2])
        m = int(input_case[0].split()[3])

        adj = [[] for i in range(E)]
        for i in range(E):
            if i == E:
                break
            a = int(input_case[i+1].split()[0])
            b = int(input_case[i+1].split()[1])
            t = int(input_case[i+1].split()[2])
            adj[a].append([b, t])
            adj[b].append([a, t])

        fire = [0 for i in range(1002)]
        for i in range(n):
            fire[i] = int(input_case[E+1].split()[i])

        for i in range(m):
            num = int(input_case[E+2].split()[i])
            adj[0].append([num, 0])
            adj[num].append([0, 0])

        dist = self.dijkstra(V, adj, 0)
        ret = 0
        for i in range(n):
            ret = ret + dist[fire[i]]

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
            E = int(datas[1])
            parsed_input_case_list.append(
                input_case_list[cursor:cursor+E+2+1]
            )
            cursor = cursor+E+1
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
            answer = int(self.output_case_list[t])
            print(str(answer)+"\t"+str(result)+"\t"+str(answer == result))


if __name__ == '__main__':
    '''
    problem link: https://algospot.com/judge/problem/read/ROUTING
    '''

    input_cases = \
        '''1
        8 12 3 2
        1 2 3
        1 6 9
        2 3 6
        3 4 4
        3 5 2
        4 5 7
        6 5 5
        8 6 5
        6 7 3
        8 7 3
        7 5 1
        2 8 3
        2 3 5
        4 6'''

    output_cases = \
        '''1
        16'''

    tester = Tester()
    solver = Solver()

    tester.set_input_cases(input_cases)
    tester.set_output_cases(output_cases)

    tester.test_solver(solver)
