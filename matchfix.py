class Solver:
    def __init__(self):
        self.INF = 2000000000

    def adjust(self, n, m, capa):
        for i in range(m+1, m+n+1):
            capa[i][m+n+1] = capa[i][m+n+1] + 1
        self.bot = self.bot + 1

    def network_flow(self, n, m, source, sink, capa, flow):
        count = 0
        while True:
            parent = [-1 for i in range(n+m+2)]
            q = [source]
            parent[source] = source
            while len(q) != 0 and parent[sink] == -1:
                here = q.pop(0)
                for there in range(n+m+1+1):
                    condition = (capa[here][there]-flow[here][there]) > 0
                    if condition and parent[there] == -1:
                        q.append(there)
                        parent[there] = here

            if parent[sink] == -1:
                if count < m:
                    self.adjust(n, m, capa)
                    continue
                else:
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

            count = count + 1

        if (capa[m+1][m+n+1] - flow[m+1][m+n+1]) > 0:
            return False
        return True

    def solve(self, input_case):
        n = int(input_case[0].split(' ')[0])
        m = int(input_case[0].split(' ')[1])
        base = [int(x) for x in input_case[1].split(' ')]
        capa = [[0 for i in range(n+m+2)] for j in range(n+m+2)]
        flow = [[0 for i in range(n+m+2)] for j in range(n+m+2)]

        self.bot = base[0]
        for i in range(1, n):
            if self.bot <= base[i]:
                self.bot = base[i] + 1

        capa[m+1][m+n+1] = self.bot - base[0]
        for i in range(m+2, n+m+1):
            capa[i][n+m+1] = self.bot-base[i-m-1]-1

        for i in range(1, m+1):
            x = int(input_case[1+i].split(' ')[0])
            y = int(input_case[1+i].split(' ')[1])
            capa[0][i] = 1
            capa[i][m+x+1] = 1
            capa[i][m+y+1] = 1

        flag = self.network_flow(n, m, 0, n+m+1, capa, flow)
        if flag is True:
            return self.bot
        else:
            return -1


class Tester:
    def __parse_input_cases(self, input_case_list):
        self.T = int(input_case_list[0])
        input_case_list = input_case_list[1:]
        parsed_input_case_list = []
        cursor = 0
        for i in range(self.T):
            m = int(input_case_list[cursor].split(' ')[1])
            parsed_input_case_list.append(
                input_case_list[cursor:cursor+m+1+1]
            )
            cursor = cursor+m+1+1
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
    problem link: https://algospot.com/judge/problem/read/MATCHFIX
    '''

    input_cases = \
        '''3
        2 2
        3 3
        0 1
        0 1
        3 3
        4 2 2
        1 2
        1 2
        1 2
        4 4
        5 3 3 2
        0 1
        1 2
        2 3
        1 3'''

    output_cases = \
        '''3
        5
        -1
        5'''

    tester = Tester()
    solver = Solver()

    tester.set_input_cases(input_cases)
    tester.set_output_cases(output_cases)

    tester.test_solver(solver)
