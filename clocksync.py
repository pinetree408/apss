class Solver:
    def __init__(self):
        self.SWITCHS = [
            [0, 1, 2],
            [3, 7, 9, 11],
            [4, 10, 14, 15],
            [0, 4, 5, 6, 7],
            [6, 7, 8, 10, 12],
            [0, 2, 14, 15],
            [3, 14, 15],
            [4, 5, 7, 14, 15],
            [1, 2, 3, 4, 5],
            [3, 4, 5, 9, 13],
        ]
        self.INF = 9999

    def is_aligned(slef, clock_list):
        if sum(clock_list) == len(clock_list) * 12:
            return True
        else:
            return False

    def push(self, clock_list, switch_id):
        for clock in self.SWITCHS[switch_id]:
            clock_list[clock] += 3
            if clock_list[clock] == 15:
                clock_list[clock] = 3

    def __solve(self, clock_list, switch_id):
        if (switch_id == len(self.SWITCHS)):
            return (0 if self.is_aligned(clock_list) else self.INF)
        ret = self.INF
        for i in range(4):
            ret = min([ret, i + self.__solve(clock_list, switch_id + 1)])
            self.push(clock_list, switch_id)
        return ret

    def solve(self, input_case):
        return self.__solve(input_case, 0)


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
            parsed_input_case = list(
                map(lambda x: int(x), input_case_list[i].split(' '))
            )
            parsed_input_case_list.append(parsed_input_case)
        return parsed_input_case_list

    def __parse_output_cases(self, output_cases):
        output_case_list = list(
            map(
                lambda x: int(x.strip()),
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
    problem link: https://algospot.com/judge/problem/read/CLOCKSYNC
    '''

    input_cases = \
        '''2
        12 6 6 6 6 6 12 12 12 12 12 12 12 12 12 12
        12 9 3 12 6 6 9 3 12 9 12 9 12 12 6 6'''

    output_cases = \
        '''2
        2
        9'''

    tester = Tester()
    solver = Solver()

    tester.set_input_cases(input_cases)
    tester.set_output_cases(output_cases)

    tester.test_solver(solver)
