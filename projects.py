class Solver:
    def __init__(self):
        self.INF = 2000000000

    def network_flow(self, n, m, source, sink, capa, flow):
        total_flow = 0
        while True:
            parent = [-1 for i in range(n+m+2)]
            q = [source]
            parent[source] = source
            while len(q) != 0 and parent[sink] == -1:
                here = q.pop(0)
                for there in range(n+m+2):
                    condition = (capa[here][there]-flow[here][there]) > 0
                    if condition and parent[there] == -1:
                        q.append(there)
                        parent[there] = here

            if parent[sink] == -1:
                break

            amt = self.INF
            p = sink
            while p != source:
                amt = min(amt, capa[parent[p]][p]-flow[parent[p]][p])
                p = parent[p]
            p = sink
            while p != source:
                flow[parent[p]][p] = flow[parent[p]][p] + amt
                flow[p][parent[p]] = flow[p][parent[p]] - amt
                p = parent[p]

            total_flow = total_flow + amt

        return total_flow

    def solve(self, input_case):
        n = int(input_case[0].split(' ')[0])
        m = int(input_case[0].split(' ')[1])
        profit = [int(x) for x in input_case[1].split(' ')]
        cost = [int(x) for x in input_case[2].split(' ')]
        capa = [[0 for i in range(n+m+2)] for j in range(n+m+2)]
        flow = [[0 for i in range(n+m+2)] for j in range(n+m+2)]

        for i in range(n):
            capa[0][2+i] = profit[i]
        for i in range(m):
            capa[2+n+i][1] = cost[i]

        requires = [[0 for j in range(m)] for i in range(n)]
        for i in range(n):
            items = [int(x) for x in input_case[3+i].split(' ')]
            for j in range(m):
                requires[i][j] = items[j]
                if requires[i][j]:
                    capa[2+i][2+n+j] = self.INF
        c = self.network_flow(n, m, 0, 1, capa, flow)
        m = sum(profit)

        return m-c


class Tester:
    def __parse_input_cases(self, input_case_list):
        self.T = int(input_case_list[0])
        input_case_list = input_case_list[1:]
        parsed_input_case_list = []
        cursor = 0
        for i in range(self.T):
            n = int(input_case_list[cursor].split(' ')[0])
            parsed_input_case_list.append(
                input_case_list[cursor:cursor+2+n+1]
            )
            cursor = cursor+2+n+1
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
            answer = int(self.output_case_list[t])
            print(str(answer)+"\t"+str(result)+"\t"+str(answer == result))


if __name__ == '__main__':
    '''
    problem link: no link
    '''

    input_cases = \
        '''2
        2 2
        10 10
        5 10
        1 0
        1 1
        5 5
        260 60 140 350 500
        250 100 150 300 100
        1 0 0 0 0
        1 1 1 0 0
        0 0 1 1 0
        0 0 0 1 0
        0 0 0 1 1'''

    output_cases = \
        '''2
        5
        460'''

    tester = Tester()
    solver = Solver()

    tester.set_input_cases(input_cases)
    tester.set_output_cases(output_cases)

    tester.test_solver(solver)
