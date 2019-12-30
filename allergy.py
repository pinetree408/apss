class Solver:
    def __init__(self):
        self.best = 0

    def search(self, can_eat, eaters, edible, chosen):
        if chosen >= self.best:
            return
        first = 0
        while first < len(can_eat) and edible[first] > 0:
            first = first + 1
        if first == len(can_eat):
            self.best = chosen
            return
        for i in range(len(can_eat[first])):
            food = can_eat[first][i]
            for j in range(len(eaters[food])):
                edible[eaters[food][j]] = edible[eaters[food][j]] + 1
            self.search(can_eat, eaters, edible, chosen+1)
            for j in range(len(eaters[food])):
                edible[eaters[food][j]] = edible[eaters[food][j]] - 1

    def solve(self, input_case):
        input_case_info = input_case[0].split(' ')
        n = int(input_case_info[0])
        m = int(input_case_info[1])
        name_list = input_case[1].split(' ')

        food_info_list = []
        for i in range(m):
            food_info_list.append(input_case[1+i+1].split(' ')[1:])

        can_eat = [[] for i in range(n)]
        for friend_idx, friend in enumerate(name_list):
            for food_info_idx, food_info in enumerate(food_info_list):
                if friend in food_info:
                    can_eat[friend_idx].append(food_info_idx)

        eaters = [[] for i in range(m)]
        for food_info_idx, food_info in enumerate(food_info_list):
            for friend_idx, friend in enumerate(name_list):
                if friend in food_info:
                    eaters[food_info_idx].append(friend_idx)

        self.best = m
        edible = [0 for i in range(n)]
        chosen = 0
        self.search(can_eat, eaters, edible, chosen)
        return self.best


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
        cursor = 0
        parsed_input_case_list = []
        for i in range(self.T):
            input_info = input_case_list[cursor].split(' ')
            m = int(input_info[1])
            parsed_input_case = input_case_list[cursor:cursor+1+m+1]
            parsed_input_case_list.append(parsed_input_case)
            cursor = cursor+1+m+1
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
    problem link: https://algospot.com/judge/problem/read/ALLERGY
    '''

    input_cases = \
        '''2
        4 6
        cl bom dara minzy
        2 dara minzy
        2 cl minzy
        2 cl dara
        1 cl
        2 bom dara
        2 bom minzy
        10 7
        a b c d e f g h i j
        6 a c d h i j
        3 a d i
        7 a c f g h i j
        3 b d g
        5 b c f h i
        4 b e g j
        5 b c g h i'''

    output_cases = \
        '''2
        2
        3'''

    tester = Tester()
    solver = Solver()

    tester.set_input_cases(input_cases)
    tester.set_output_cases(output_cases)

    tester.test_solver(solver)
