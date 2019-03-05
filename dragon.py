MAX_LEN = 1000000001
LEN = [0 for i in range(51)]


def pre_calc():
    LEN[0] = 1
    for i in range(1, 51):
        LEN[i] = min(MAX_LEN, LEN[i-1]*2+2)


def expand(dragon, generation, skip):
    if generation == 0:
        return dragon[skip]

    for i in range(len(dragon)):
        if dragon[i] == 'X' or dragon[i] == 'Y':
            if skip >= LEN[generation]:
                skip = skip - LEN[generation]
            elif dragon[i] == 'X':
                return expand('X+YF', generation - 1, skip)
            else:
                return expand('FX-Y', generation - 1, skip)
        elif skip > 0:
            skip = skip - 1
        else:
            return dragon[i]


def dragon(input_case):
    input_list = list(
        map(
            lambda x: x.strip(),
            input_case.split('\n')
        )
    )
    case_num = int(input_list[0])
    input_list = input_list[1:]

    pre_calc()

    for i in range(case_num):
        n = int(input_list[i].split(' ')[0])
        p = int(input_list[i].split(' ')[1])
        length = int(input_list[i].split(' ')[2])
        result = []
        for j in range(p - 1, p + length - 1):
            result.append(expand("FX", n, j))
        print "".join(result)


if __name__ == '__main__':
    input_case = \
        '''4
        0 1 2
        1 1 5
        2 6 5
        42 764853475 30'''
    dragon(input_case)
