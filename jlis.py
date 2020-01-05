class Solver:
    def merge_list(self, a_idx, b_idx, a_list, b_list):
        if a_idx == -1:
            a = -1
        else:
            a = a_list[a_idx]
        if b_idx == -1:
            b = -1
        else:
            b = b_list[b_idx]

        ret = 2
        max_item = max(a, b)

        for i in range(a_idx+1, len(a_list)):
            if max_item < a_list[i]:
                ret = max(ret, self.merge_list(i, b_idx, a_list, b_list) + 1)
        for i in range(b_idx+1, len(b_list)):
            if max_item < b_list[i]:
                ret = max(ret, self.merge_list(a_idx, i, a_list, b_list) + 1)
        return ret

    def solve(self, input_case):
        a_list = list(map(lambda x: int(x), input_case[0].split(' ')))
        b_list = list(map(lambda x: int(x), input_case[1].split(' ')))
        return self.merge_list(-1, -1, a_list, b_list) - 2


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
            parsed_input_case_list.append([
                input_case_list[i*3+1],
                input_case_list[i*3+2]
            ])
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
    problem link: https://algospot.com/judge/problem/read/JLIS
    '''

    input_cases = \
        '''3
        3 3
        1 2 4
        3 4 7
        3 3
        1 2 3
        4 5 6
        5 3
        10 20 30 1 2
        10 20 30'''

    output_cases = \
        '''3
        5
        6
        5'''

    tester = Tester()
    solver = Solver()

    tester.set_input_cases(input_cases)
    tester.set_output_cases(output_cases)

    tester.test_solver(solver)
