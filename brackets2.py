def solve(formula):
    opening = '({['
    closing = ')}]'
    stack = []
    for i in range(len(formula)):
        if formula[i] in opening:
            stack.append(formula[i])
        else:
            if len(stack) == 0:
                return False
            top_idx = len(stack)-1
            if opening.index(stack[top_idx]) != closing.index(formula[i]):
                return False
            stack.pop()
    return len(stack) == 0


def brackets2(input_case):
    global CACHE
    input_list = list(
        map(
            lambda x: [i for i in x.strip().split(' ')],
            input_case.split('\n')
        )
    )
    case_num = int(input_list[0][0])
    input_list = input_list[1:]

    for i in range(case_num):
        print solve(input_list[i][0])


if __name__ == '__main__':
    input_case = \
        '''3
        ()()
        ({[}])
        ({}[(){}])'''
    brackets2(input_case)
