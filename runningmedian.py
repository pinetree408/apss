def solve(n, a, b):
    right = []
    left = []
    curr = 1983
    median = 1983
    result = 1983

    for i in range(n-1):
        curr = (curr*a+b) % 20090711
        if curr > median:
            right.append(curr)
        else:
            left.append(curr)
        diff = len(left) - len(right)
        if diff > 0:
            right.append(median)
            right.sort()
            left.sort(reverse=True)
            median = left[0]
            left.pop(0)
        elif diff < -1:
            left.append(median)
            left.sort(reverse=True)
            right.sort()
            median = right[0]
            right.pop(0)
        result = (result+median) % 20090711
    return result


def runningmedian(input_case):
    input_list = list(
        map(
            lambda x: [int(i) for i in x.strip().split(' ')],
            input_case.split('\n')
        )
    )
    case_num = int(input_list[0][0])
    input_list = input_list[1:]

    for i in range(case_num):
        n = input_list[i][0]
        a = input_list[i][1]
        b = input_list[i][2]
        print solve(n, a, b)


if __name__ == '__main__':
    input_case = \
        '''3
        10 1 0
        10 1 1
        10000 1273 4936'''
    runningmedian(input_case)
