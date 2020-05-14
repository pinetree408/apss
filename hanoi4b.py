class Solver:
    def set(self, state, index, value):
        return (state & ~(3 << (index*2))) | (value << (index*2))

    def get(self, state, index):
        return (state >> (index*2)) & 3

    def sgn(self, x):
        if not x:
            return 0
        return (x > 0) if 1 else -1

    def incr(self, x):
        if x < 0:
            return x - 1
        return x + 1

    def bidir(self, discs, begin, end):
        if begin == end:
            return 0
        q = []
        c = [0 for i in range(1 << (12*2))]

        q.append(begin)
        c[begin] = 1
        q.append(end)
        c[end] = -1

        while len(q) != 0:
            here = q.pop(0)
            top = [-1, -1, -1, -1]
            for i in reversed(range(discs)):
                top[self.get(here, i)] = i
            for i in range(4):
                if top[i] != -1:
                    for j in range(4):
                        if i != j and (top[j] == -1 or top[j] > top[i]):
                            there = self.set(here, top[i], j)
                            if c[there] == 0:
                                c[there] = self.incr(c[here])
                                q.append(there)
                            elif self.sgn(c[there]) != self.sgn(c[here]):
                                return abs(c[there]) + abs(c[here]) - 1
        return -1

    def solve(self, input_case):
        N = int(input_case[0])
        first = 0
        end = pow(2, 2*N) - 1
        for i in range(len(input_case[1:])):
            temp = input_case[1+i].split(" ")
            for j in range(int(temp[0])):
                n = int(temp[1+j])
                first = self.set(first, n-1, i)
        ret = self.bidir(N, first, end)

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
        for i in range(self.T):
            parsed_input_case_list.append(input_case_list[i*5:(i+1)*5])
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
    problem link: https://algospot.com/judge/problem/read/HANOI4
    '''

    input_cases = \
        '''3
        5
        1 1
        1 3
        2 5 4
        1 2
        3
        1 2
        0
        2 3 1
        0
        10
        2 8 7
        2 5 4
        3 6 3 2
        3 10 9 1'''

    output_cases = \
        '''3
        10
        4
        24'''

    tester = Tester()
    solver = Solver()

    tester.set_input_cases(input_cases)
    tester.set_output_cases(output_cases)

    tester.test_solver(solver)
