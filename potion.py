def gcd(a, b):
    return a if b == 0 else gcd(b, a % b)


def ceil(a, b):
    return (a + b - 1) / b


def solve(recipe_list, put_list):
    b = recipe_list[0]
    for i in range(1, len(recipe_list)):
        b = gcd(b, recipe_list[i])

    a = b
    for i in range(len(recipe_list)):
        a = max(a, ceil(put_list[i] * b, recipe_list[i]))

    ret = []
    for i in range(len(recipe_list)):
        ret.append(recipe_list[i] * a / b - put_list[i])
    return ret


def potion(input_case):
    input_list = list(
        map(
            lambda x: [int(i) for i in x.strip().split(' ')],
            input_case.split('\n')
        )
    )
    case_num = int(input_list[0][0])
    input_list = input_list[1:]

    for i in range(case_num):
        recipe_list = input_list[i*3+1]
        put_list = input_list[i*3+2]
        print solve(recipe_list, put_list)


if __name__ == '__main__':
    input_case = \
        '''3
        4
        4 6 2 4
        6 4 2 4
        4
        4 6 2 4
        7 4 2 4
        3
        4 5 6
        1 2 3'''
    potion(input_case)
