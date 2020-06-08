class Solver:
    def is_range(self, y, x):
        return not (y < 0 or x < 0 or y >= self.h or x >= self.w)

    def dfs(self, a):
        if self.visited[a] == self.visitcnt:
            return False
        self.visited[a] = self.visitcnt
        for b in range(self.m):
            if self.adj[a][b]:
                if self.b_match[b] == -1 or self.dfs(self.b_match[b]):
                    self.a_match[a] = b
                    self.b_match[b] = a
                    return True
        return False

    def bipartite(self):
        size = 0
        self.visitcnt = 0
        self.visited = [0 for i in range(401)]
        self.a_match = [-1 for i in range(401)]
        self.b_match = [-1 for i in range(401)]

        for i in range(self.n):
            self.visitcnt = self.visitcnt + 1
            if self.dfs(i):
                size = size + 1

        return size

    def solve(self, input_case):
        self.idx = [
            [[-1 for i in range(401)] for j in range(401)] for k in range(2)
        ]
        self.adj = [[0 for i in range(401)] for j in range(401)]
        self.h = int(input_case[0].split(' ')[0])
        self.w = int(input_case[0].split(' ')[1])
        self.board = [input_case[1+i] for i in range(self.h)]
        self.n = 0
        self.m = 0

        for i in range(self.h):
            for j in range(self.w):
                if self.board[i][j] == ".":
                    if (i+j) % 2 == 0:
                        self.idx[0][i][j] = self.n
                        self.n = self.n + 1
                    else:
                        self.idx[1][i][j] = self.m
                        self.m = self.m + 1

        dy = [0, 1]
        dx = [1, 0]
        for i in range(self.h):
            for j in range(self.w):
                if self.board[i][j] == ".":
                    for k in range(2):
                        ny = i + dy[k]
                        nx = j + dx[k]
                        if self.is_range(ny, nx) and\
                                self.board[ny][nx] == ".":
                            if (i+j) % 2 == 0:
                                temp_y = self.idx[0][i][j]
                                temp_x = self.idx[1][ny][nx]
                                self.adj[temp_y][temp_x] = 1
                            else:
                                temp_y = self.idx[0][ny][nx]
                                temp_x = self.idx[1][i][j]
                                self.adj[temp_y][temp_x] = 1
        c = self.bipartite()
        a_chosen = [True for i in range(self.n)]
        b_chosen = [False for i in range(self.m)]
        for i in range(self.m):
            if self.b_match[i] == -1:
                b_chosen[i] = True

        changed = False
        while True:
            changed = False
            for i in range(self.n):
                for j in range(self.m):
                    if a_chosen[i] and b_chosen[j] and self.adj[i][j]:
                        b_chosen[self.a_match[i]] = True
                        a_chosen[i] = False
                        changed = True
            if not changed:
                break

        cnt = 0
        ret_str = []
        for i in range(self.h):
            ret_str_row = []
            for j in range(self.w):
                if self.board[i][j] == "#":
                    ret_str_row.append("#")
                else:
                    if (i+j) % 2 == 0:
                        if a_chosen[self.idx[0][i][j]]:
                            ret_str_row.append("^")
                            cnt = cnt + 1
                        else:
                            ret_str_row.append(".")
                    else:
                        if b_chosen[self.idx[1][i][j]]:
                            ret_str_row.append("^")
                            cnt = cnt + 1
                        else:
                            ret_str_row.append(".")
            ret_str.append("".join(ret_str_row))
        return [cnt, ret_str]


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
        cursor = 0
        for t in range(self.T):
            result = solver.solve(self.input_case_list[t])
            ret_cnt = result[0]
            ret_map = result[1]
            answer = int(self.output_case_list[cursor])
            is_correct = str(answer == ret_cnt)
            print(
                str(answer)+"\t"+str(ret_cnt)+"\t"+is_correct
            )
            for i in range(len(ret_map)):
                answer = self.output_case_list[cursor+1+i]
                is_correct = str(answer == ret_map[i])
                print(ret_map[i]+"\t"+answer+"\t"+is_correct)
            cursor = cursor + len(ret_map) + 1


if __name__ == '__main__':
    '''
    problem link: https://algospot.com/judge/problem/read/TRAPCARD
    '''

    input_cases = \
        '''2
        5 3
        ...
        #.#
        #.#
        #.#
        ...
        6 10
        ###.###.##
        .##.....#.
        ..#.###...
        ..###..##.
        .####..#.#
        ..........'''

    output_cases = \
        '''2
        6
        ^.^
        #^#
        #.#
        #^#
        ^.^
        19
        ###^###^##
        .##.^.^.#^
        ^.#^###.^.
        .^###^.##^
        ^####.^#^#
        .^.^.^.^.^'''

    tester = Tester()
    solver = Solver()

    tester.set_input_cases(input_cases)
    tester.set_output_cases(output_cases)

    tester.test_solver(solver)
