class Solver:
    def __init__(self):
        self.INF = 987654321

    def solve(self, input_case):
        v = int(input_case[0].split(' ')[0])
        n = int(input_case[0].split(' ')[1])
        m = int(input_case[0].split(' ')[2])
        adj = [[self.INF for i in range(v)] for j in range(v)]
        for i in range(v):
            adj[i][i] = 0
        for i in range(n):
            x = int(input_case[1+i].split(' ')[0])
            y = int(input_case[1+i].split(' ')[1])
            r = int(input_case[1+i].split(' ')[2])
            if adj[x][y] > r:
                adj[x][y] = r
                adj[y][x] = r
        for k in range(v):
            for i in range(v):
                for j in range(v):
                    adj[i][j] = min(adj[i][j], adj[i][k] + adj[k][j])
        ret = 0
        for i in range(m):
            x = int(input_case[1+n+i].split(' ')[0])
            y = int(input_case[1+n+i].split(' ')[1])
            r = int(input_case[1+n+i].split(' ')[2])
            if adj[x][y] <= r:
                ret = ret + 1
                break
            else:
                for i in range(v):
                    for j in range(v):
                        adj[i][j] = min(
                            adj[i][j],
                            min(
                                adj[i][x] + r + adj[y][j],
                                adj[i][y] + r + adj[x][j]
                            )
                        )
        return ret


class Tester:
    def __parse_input_cases(self, input_case_list):
        self.T = int(input_case_list[0])
        input_case_list = input_case_list[1:]
        parsed_input_case_list = []
        cursor = 0
        for i in range(self.T):
            n = int(input_case_list[cursor].split(' ')[1])
            m = int(input_case_list[cursor].split(' ')[2])
            parsed_input_case_list.append(
                input_case_list[cursor:cursor+n+m+1]
            )
            cursor = cursor+n+m+1
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
    problem link: https://algospot.com/judge/problem/read/PROMISES
    '''

    input_cases = \
        '''2
        4 2 2
        0 1 4
        0 3 1
        0 2 2
        1 2 6
        4 2 2
        0 1 4
        0 3 1
        1 2 6
        0 2 2'''

    output_cases = \
        '''2
        1
        0'''

    tester = Tester()
    solver = Solver()

    tester.set_input_cases(input_cases)
    tester.set_output_cases(output_cases)

    tester.test_solver(solver)
