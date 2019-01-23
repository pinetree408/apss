CACHE = [[]]
CHOICE = [[]]


def recognize(segment, prev_match, R, T, M):
    global CACHE, CHOICE
    if segment == len(R):
        return 0
    if CACHE[segment][prev_match] != 1.0:
        return CACHE[segment][prev_match]
    CACHE[segment][prev_match] = -1e200
    for this_match in range(1, len(M)):
        cand =\
            T[prev_match][this_match - 1] +\
            M[this_match][R[segment]] +\
            recognize(
                segment + 1, this_match,
                R, T, M
            )
        if CACHE[segment][prev_match] < cand:
            CACHE[segment][prev_match] = cand
            CHOICE[segment][prev_match] = this_match
    return CACHE[segment][prev_match]


def reconstruct(segment, prev_match, corpus, R):
    global CHOICE
    ret = corpus[CHOICE[segment][prev_match] - 1]
    if segment < len(R) - 1:
        ret = ret + " " +\
            reconstruct(
                segment + 1, CHOICE[segment][prev_match], corpus, R
            )
    return ret


def ocr(input_case):
    global CACHE, CHOICE
    input_list = list(
        map(
            lambda x: [str(i) for i in x.strip().split(' ')],
            input_case.split('\n')
        )
    )
    word_num = int(input_list[0][0])
    word_list = input_list[1]
    T = input_list[2:2 + word_num + 1]
    T = list(
        map(
            lambda x: [float(i) for i in x],
            T
        )
    )
    M = input_list[2 + word_num:2 + word_num + 1 + word_num]
    M = list(
        map(
            lambda x: [float(i) for i in x],
            M
        )
    )
    case_list = input_list[2 + word_num + 1 + word_num:]
    for case in case_list:
        target = case[1:]
        R = list(
            map(
                lambda x: word_list.index(x),
                target
            )
        )
        CACHE = [[1 for j in range(len(M))] for i in range(len(R))]
        CHOICE = [[-1 for j in range(len(M))] for i in range(len(R))]
        recognize(0, 0, R, T, M)
        print reconstruct(0, 0, word_list, R)


if __name__ == '__main__':
    input_case = \
        '''5 3
        I am a boy buy
        1.0 0.0 0.0 0.0 0.0
        0.1 0.6 0.1 0.1 0.1
        0.1 0.1 0.6 0.1 0.1
        0.1 0.1 0.1 0.6 0.1
        0.2 0.2 0.2 0.2 0.2
        0.2 0.2 0.2 0.2 0.2
        0.8 0.1 0.0 0.1 0.0
        0.1 0.7 0.0 0.2 0.0
        0.0 0.1 0.8 0.0 0.1
        0.0 0.0 0.0 0.5 0.5
        0.0 0.0 0.0 0.5 0.5
        4 I am a buy
        4 I I a boy
        4 I am am boy'''
    ocr(input_case)
