class Solver:
    def __append(self, here, edge, mod):
        there = here*10+edge
        if there >= mod:
            return mod + there % mod
        else:
            return there % mod

    def solve(self, input_case):
        d = list(
            map(
                lambda x: str(x),
                input_case[0]
            )
        )
        n = int(input_case[1])
        m = int(input_case[2])

        d.sort()

        parent = [-1 for i in range(2*n)]
        choice = [-1 for i in range(2*n)]
        q = []

        parent[0] = 0
        q.append(0)

        while len(q) != 0:
            here = q.pop(0)
            for i in range(0, len(d)):
                there = self.__append(here, ord(chr(ord(d[i]) - ord('0'))), n)
                if parent[there] == -1:
                    parent[there] = here
                    choice[there] = chr(ord(d[i]) - ord('0'))
                    q.append(there)
        if parent[n+m] == -1:
            return "IMPOSSIBLE"
        ret = []
        here = n+m
        while parent[here] != here:
            ret.append(chr(ord('0') + ord(choice[here])))
            here = parent[here]
        ret.reverse()

        return "".join(ret)


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
        for i in range(self.T):
            input_info = input_case_list[i].split(' ')
            parsed_input_case = list(
                map(
                    lambda x: x.strip(),
                    input_info
                )
            )
            parsed_input_case_list.append(parsed_input_case)
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
            print(answer+"\t"+result+"\t"+str(answer == result))


if __name__ == '__main__':
    '''
    problem link: https://algospot.com/judge/problem/read/CHILDRENDAY
    '''

    input_cases = \
        '''5
        1 7 0
        1 10 1
        0 7 3
        345 9997 3333
        35 9 8'''

    output_cases = \
        '''5
        111111
        11
        IMPOSSIBLE
        35355353545
        35'''

    tester = Tester()
    solver = Solver()

    tester.set_input_cases(input_cases)
    tester.set_output_cases(output_cases)

    tester.test_solver(solver)
