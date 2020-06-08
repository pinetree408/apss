class Solver:
    def mutate(self, board, n_to_id):
        dy = [1, 1]
        dx = [-1, 1]
        cnt = [0, 0]
        for y in range(len(board)):
            for x in range(len(board[0])):
                for d in range(2):
                    if board[y][x] == "." and n_to_id[y][x][d] == -1:
                        y_temp = y
                        x_temp = x
                        while True:
                            if y_temp < 0:
                                break
                            if y_temp >= len(board):
                                break
                            if x_temp < 0:
                                break
                            if x_temp >= len(board):
                                break
                            if board[y_temp][x_temp] != ".":
                                break
                            n_to_id[y_temp][x_temp][d] = cnt[d]
                            y_temp = y_temp + dy[d]
                            x_temp = x_temp + dx[d]
                        cnt[d] = cnt[d] + 1

        for y in range(len(board)):
            for x in range(len(board[0])):
                if board[y][x] == ".":
                    self.adj[n_to_id[y][x][0]][n_to_id[y][x][1]] = 1

        return cnt

    def dfs(self, cnt, visited, a_match, b_match, here):
        if visited[here]:
            return False
        visited[here] = True
        for dst in range(cnt[1]):
            if self.adj[here][dst]:
                if b_match[dst] == -1 or\
                        self.dfs(
                            cnt, visited, a_match, b_match, b_match[dst]
                        ):
                    a_match[here] = dst
                    b_match[dst] = here
                    return True
        return False

    def bitmatch(self, cnt):
        a_match = [-1 for i in range(cnt[0])]
        b_match = [-1 for i in range(cnt[1])]
        size = 0
        for start in range(cnt[0]):
            visited = [False for i in range(cnt[0])]
            if self.dfs(cnt, visited, a_match, b_match, start):
                size = size+1
        return size

    def solve(self, input_case):
        n = int(input_case[0].split(' ')[0])
        board = []
        n_to_id = [[[-1, -1] for j in range(n)] for i in range(n)]
        self.adj = [[0 for j in range(n*n)] for i in range(n*n)]
        for i in range(n):
            row = input_case[i+1]
            board.append(row)
        cnt = self.mutate(board, n_to_id)
        ret = self.bitmatch(cnt)
        return ret


class Tester:
    def __parse_input_cases(self, input_case_list):
        self.T = int(input_case_list[0])
        input_case_list = input_case_list[1:]
        parsed_input_case_list = []
        cursor = 0
        for i in range(self.T):
            n = int(input_case_list[cursor].split(' ')[0])
            parsed_input_case_list.append(
                input_case_list[cursor:cursor+n+1]
            )
            cursor = cursor+n+1
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
    problem link: https://www.algospot.com/judge/problem/read/BISHOPS
    '''

    input_cases = \
        '''3
        5
        .....
        .....
        .....
        .....
        .....
        8
        ..**.*.*
        **.***.*
        *.**...*
        .*.**.**
        *.**.*.*
        ..**.*.*
        ...*.*.*
        **.*.*.*
        8
        *.*.*.*.
        .*.*.*.*
        *.*.*.*.
        .*.*.*.*
        *.*.*.*.
        .*.*.*.*
        *.*.*.*.
        .*.*.*.*'''

    output_cases = \
        '''3
        8
        18
        7'''

    tester = Tester()
    solver = Solver()

    tester.set_input_cases(input_cases)
    tester.set_output_cases(output_cases)

    tester.test_solver(solver)
