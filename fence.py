def fence(input_case):
    input_list = list(
        map(
            lambda x: x.strip(),
            input_case.split('\n')
        )
    )
    case_num = int(input_list[0])
    input_list = input_list[1:]
    for i in range(case_num):
        fence_list = list(
            map(
                lambda x: int(x),
                input_list[i*2 + 1].split(' ')
            )
        )
        result = []
        for j, item in enumerate(fence_list):
            source = fence_list[j]
            width = 0
            prev_index = j
            for left in range(0, j):
                target = fence_list[j - 1 - left]
                if source <= target and prev_index - (j - 1 - left) == 1:
                    width += 1
                    prev_index = (j - 1 - left)
                else:
                    break
            prev_index = j
            for right in range(j + 1, len(fence_list)):
                target = fence_list[right]
                if source <= target and right - prev_index == 1:
                    width += 1
                    prev_index = right
                else:
                    break
            result.append((width + 1) * source)
        print max(result)


if __name__ == '__main__':
    input_case = \
        '''3
        7
        7 1 5 9 6 7 3
        7
        1 4 4 4 4 4 4
        4
        1 8 2 2'''
    fence(input_case)
