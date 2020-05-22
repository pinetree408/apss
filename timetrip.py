class Solver:
    def __init__(self):
        self.INF = 987654321

    def __solve_min(self, v, w, e, reachable):
        dist = [self.INF for i in range(v)]
        dist[0] = 0
        for k in range(v-1):
            for here in range(v):
                for there, cost in e[here]:
                    if dist[there] > dist[here] + cost:
                        dist[there] = dist[here] + cost

        for here in range(v):
            for there, cost in e[here]:
                if dist[there] > dist[here] + cost:
                    if reachable[0][here] and reachable[here][1]:
                        return self.INF

        return dist[1]

    def solve(self, input_case):
        v = int(input_case[0].split(' ')[0])
        w = int(input_case[0].split(' ')[1])
        e = [[] for i in range(v)]
        e_neg = [[] for i in range(v)]
        reachable = [[False for i in range(v)] for j in range(v)]

        for i in range(w):
            a = int(input_case[i+1].split(' ')[0])
            b = int(input_case[i+1].split(' ')[1])
            d = int(input_case[i+1].split(' ')[2])
            e[a].append([b, d])
            e_neg[a].append([b, -d])
            reachable[a][b] = True
        for k in range(v):
            for i in range(v):
                for j in range(v):
                    reachable[i][j] = reachable[i][j] or\
                        (reachable[i][k] and reachable[k][j])
        if not reachable[0][1]:
            return "UNREACHABLE"

        ret = self.__solve_min(v, w, e, reachable)
        ret_neg = -self.__solve_min(v, w, e_neg, reachable)
        max_value = self.INF - 1
        if ret > max_value:
            ret = 'INFINITY'
        if abs(ret_neg) > max_value:
            ret_neg = 'INFINITY'

        return str(ret) + ' ' + str(ret_neg)


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
            num = int(input_case_list[cursor].split(' ')[1])
            parsed_input_case_list.append(
                input_case_list[cursor:cursor+num+1]
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
    problem link: https://algospot.com/judge/problem/read/TIMETRIP
    '''

    input_cases = \
        '''4
        2 2
        0 1 1
        0 1 3
        4 4
        0 2 -7
        0 3 -4
        3 2 9
        2 1 3
        4 3
        0 2 0
        2 2 1
        2 1 0
        3 0'''

    output_cases = \
        '''4
        1 3
        -4 8
        0 INFINITY
        UNREACHABLE'''

    tester = Tester()
    solver = Solver()

    tester.set_input_cases(input_cases)
    tester.set_output_cases(output_cases)

    tester.test_solver(solver)
