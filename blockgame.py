MOVES = []
CACHE = []


def cell(y, x):
    return 1 << (y*5+x)


def precalc():
    global MOVES
    for i in range(4):
        for j in range(4):
            cells = []
            for di in range(2):
                for dj in range(2):
                    cells.append(cell(i+di, j+dj))
            square = cells[0] + cells[1] + cells[2] + cells[3]
            for k in range(4):
                MOVES.append(square - cells[k])

    for i in range(5):
        for j in range(4):
            MOVES.append(cell(i, j) + cell(i, j+1))
            MOVES.append(cell(j, i) + cell(j+1, i))


def play(board):
    global MOVES, CACHE
    if CACHE[board] != -1:
        return CACHE[board]
    CACHE[board] = 0
    for i in range(len(MOVES)):
        if (MOVES[i] & board) == 0:
            if not play(board | MOVES[i]):
                CACHE[board] = 1
                break
    return CACHE[board]


def blockgame(input_case):
    global CACHE
    input_list = list(
        map(
            lambda x: [i for i in x.strip().split(' ')],
            input_case.split('\n')
        )
    )
    case_num = int(input_list[0][0])
    input_list = input_list[1:]
    cursor = 0

    precalc()
    for i in range(case_num):
        board = input_list[cursor:5*(i+1)]
        CACHE = [-1 for j in range(1 << 25)]
        board_list = [0 for j in range(25)]
        for y in range(5):
            for x in range(5):
                if board[y][0][x] == '#':
                    board_list[y*5+x] = 1
        board_sum = 0
        for k in range(25):
            board_sum = board_sum + board_list[k] * (1 << k)
        result = play(board_sum)
        if result == 1:
            print "WINNING"
        else:
            print "LOSING"
        cursor = 5*(i+1)


if __name__ == '__main__':
    input_case = \
        '''3
        .....
        .##..
        ##..#
        #.###
        ..#..
        .....
        .....
        .....
        .....
        .....
        #..##
        ##.##
        ##.##
        #...#
        ##.##'''
    blockgame(input_case)
