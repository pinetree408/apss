CACHE_R = [[]]
CACHE_O = [[]]


def overlap(x, y):
    overlap = 0
    for i in range(len(x)):
        target_x = x[i:]
        target_y = y[:len(target_x)]
        if target_x == target_y:
            overlap = len(x) - i
            break
    return overlap


def _restore(targets, last, used):
    global CACHE_O, CACHE_R
    if used == ((1 << len(targets)) - 1):
        return 0
    if CACHE_R[last][used] != -1:
        return CACHE_R[last][used]
    for next_i in range(len(targets)):
        if (used & (1 << next_i)) == 0:
            cand = CACHE_O[last][next_i] +\
                _restore(targets, next_i, used + (1 << next_i))
            CACHE_R[last][used] = max(CACHE_R[last][used], cand)
    return CACHE_R[last][used]


def reconstruct(targets, last, used):
    global CACHE_O
    if used == ((1 << len(targets)) - 1):
        return ""
    for next_i in range(len(targets)):
        if used & (1 << next_i):
            continue
        if_used = _restore(targets, next_i, used + (1 << next_i)) +\
            CACHE_O[last][next_i]
        if _restore(targets, last, used) == if_used:
            return targets[next_i][CACHE_O[last][next_i]:] +\
                reconstruct(targets, next_i, used + (1 << next_i))


def restore(input_case):
    global CACHE_O, CACHE_R
    input_list = list(
        map(
            lambda x: [i for i in x.strip().split(' ')],
            input_case.split('\n')
        )
    )
    case_num = int(input_list[0][0])
    input_list = input_list[1:]
    cursor = 0
    for i in range(case_num):
        start = cursor
        end = start + int(input_list[start][0]) + 1
        targets = map(lambda x: x[0], input_list[start+1:end])
        for x in targets[:]:
            for y in targets[:]:
                if x != y and x in y:
                    targets.remove(x)
        targets.insert(0, "")
        CACHE_O = [
            [0 for j in range(len(targets))] for i in range(len(targets))
        ]
        CACHE_R = [
            [-1 for j in range(1<<len(targets))] for i in range(len(targets))
        ]
        for i in range(len(targets)):
            for j in range(len(targets)):
                CACHE_O[i][j] = overlap(targets[i], targets[j])
        print reconstruct(targets, 0, 0)
        cursor = end


if __name__ == '__main__':
    input_case = \
        '''3
        3
        geo
        oji
        jing
        2
        world
        hello
        3
        abrac
        cadabra
        dabr'''
    restore(input_case)
