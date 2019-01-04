cursor = -1


def reverse(input_list):
    global cursor
    cursor += 1
    if input_list[cursor] != 'x':
        return input_list[cursor]
    tree = []
    for i in range(4):
        tree.append(reverse(input_list))
    return 'x' + tree[2] + tree[3] + tree[0] + tree[1]


def quadtree(input_case):
    global cursor
    input_list = list(
        map(
            lambda x: x.strip(),
            input_case.split('\n')
        )
    )
    case_num = int(input_list[0])
    input_list = input_list[1:]
    for i in range(case_num):
        cursor = -1
        print reverse(input_list[i])


if __name__ == '__main__':
    input_case = \
        '''4
        w
        xbwwb
        xbwxwbbwb
        xxwwwbxwxwbbbwwxxxwwbbbwwwwbb'''
    quadtree(input_case)
