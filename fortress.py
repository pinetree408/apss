longest = 0


def encloses(a, b):
    return (
        (a[2] > b[2]) and
        ((pow(a[1]-b[1], 2)+pow(a[0]-b[0], 2)) < pow(a[2]-b[2], 2))
    )


def is_child(a, b, info_list):
    if not encloses(info_list[a], info_list[b]):
        return False
    for i in range(len(info_list)):
        if i != a and i != b and\
                encloses(info_list[a], info_list[i]) and\
                encloses(info_list[i], info_list[b]):
            return False
    return True


def get_tree(root, info_list):
    ret = {
        'id': root,
        'child': []
    }
    for ch in range(len(info_list)):
        if is_child(root, ch, info_list):
            ret['child'].append(get_tree(ch, info_list))
    return ret


def height(tree):
    global longest
    heights = []
    for i in range(len(tree['child'])):
        heights.append(height(tree['child'][i]))
    if len(heights) == 0:
        return 0
    heights.sort()
    if len(heights) >= 2:
        longest = max(
            longest, 2+heights[len(heights)-2]+heights[len(heights)-1]
        )
    return heights[len(heights)-1]+1


def solve(tree):
    global longest
    longest = 0
    h = height(tree)
    return max(longest, h)


def fortress(input_case):
    input_list = list(
        map(
            lambda x: [int(i) for i in x.strip().split(' ')],
            input_case.split('\n')
        )
    )
    case_num = int(input_list[0][0])
    input_list = input_list[1:]

    case_start = 0
    for i in range(case_num):
        start = case_start
        n = input_list[start][0]
        info_list = input_list[start+1:start+1+n]
        print solve(get_tree(0, info_list))
        case_start = start+1+n


if __name__ == '__main__':
    input_case = \
        '''2
        3
        5 5 15
        5 5 10
        5 5 5
        8
        21 15 20
        15 15 10
        13 12 5
        12 12 3
        19 19 2
        30 24 5
        32 10 7
        32 9 4'''
    fortress(input_case)
