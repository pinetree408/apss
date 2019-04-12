EMPTY = -987654321
CACHE = [[]]


def play(board, left, right):
    global CACHE
    if left > right:
        return 0
    if CACHE[left][right] != EMPTY:
        return CACHE[left][right]
    CACHE[left][right] = max(
        board[left] - play(board, left + 1, right),
        board[right] - play(board, left, right - 1)
    )
    if right - left >= 1:
        CACHE[left][right] = max(
            CACHE[left][right],
            -play(board, left + 2, right)
        )
        CACHE[left][right] = max(
            CACHE[left][right],
            -play(board, left, right - 2)
        )
    return CACHE[left][right]


def numbergame(input_case):
    global CACHE
    input_list = list(
        map(
            lambda x: [int(i) for i in x.strip().split(' ')],
            input_case.split('\n')
        )
    )
    case_num = int(input_list[0][0])
    input_list = input_list[1:]
    cursor = 0
    for i in range(case_num):
        board = input_list[2*i+1]
        CACHE = [
            [EMPTY for j in range(len(board))] for i in range(len(board))
        ]
        print board
        print play(board, 0, len(board)-1)


if __name__ == '__main__':
    input_case = \
        '''3
        5
        -1000 -1000 -3 -1000 -1000
        6
        100 -1000 -1000 100 -1000 -1000
        10
        7 -5 8 5 1 -4 -8 6 7 9'''
    numbergame(input_case)
