import sys


class Solver:
    def dfs(self, n, start, graph, min_v, max_v):
        if start == n-1:
            return True
        graph[start][start] = 1
        for i in range(n):
            if graph[i][i] == -1 and min_v <= graph[start][i] <= max_v:
                if self.dfs(n, i, graph, min_v, max_v):
                    graph[start][start] = -1
                    return True
        graph[start][start] = -1
        return False

    def solve(self, input_case):
        n = int(input_case[0].split(' ')[0])
        m = int(input_case[0].split(' ')[1])
        if m == 1:
            return 0
        graph = [[-1 for i in range(n)] for j in range(n)]
        orders = set()
        for i in range(m):
            v1 = int(input_case[1+i].split(' ')[0])
            v2 = int(input_case[1+i].split(' ')[1])
            cost = int(input_case[1+i].split(' ')[2])
            graph[v1][v2] = cost
            graph[v2][v1] = cost
            orders.add(cost)
        orders = list(orders)
        orders.sort()
        low = 0
        high = 0
        ret = sys.maxint
        while True:
            if self.dfs(n, 0, graph, orders[low], orders[high]):
                ret = min(ret, orders[high]-orders[low])
                low = low+1
            else:
                if high == len(orders)-1:
                    break
                high = high+1
        return ret


class Tester:
    def __parse_input_cases(self, input_case_list):
        self.T = int(input_case_list[0])
        input_case_list = input_case_list[1:]
        parsed_input_case_list = []
        cursor = 0
        for i in range(self.T):
            m = int(input_case_list[cursor].split(' ')[1])
            parsed_input_case_list.append(
                input_case_list[cursor:cursor+m+1]
            )
            cursor = cursor+m+1
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
    problem link: https://algospot.com/judge/problem/read/TPATH
    '''

    input_cases = \
        '''3
        2 1
        0 1 100
        4 3
        0 1 127
        1 2 14
        2 3 96
        4 4
        0 1 100
        1 3 99
        0 2 17
        2 3 10'''

    output_cases = \
        '''3
        0
        113
        1'''

    tester = Tester()
    solver = Solver()

    tester.set_input_cases(input_cases)
    tester.set_output_cases(output_cases)

    tester.test_solver(solver)
