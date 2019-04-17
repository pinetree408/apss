CACHE = []


def _sushi(m, price_pref_set):
    global CACHE
    ret = 0
    CACHE[0] = 0
    m = m/100
    for budget in range(1, m+1):
        cand = 0
        for dish in range(len(price_pref_set)):
            price = price_pref_set[dish][0]/100
            pref = price_pref_set[dish][1]
            if budget >= price:
                cand = max(
                    cand,
                    CACHE[(budget-price) % 201] + pref
                )
        CACHE[budget % 201] = cand
        ret = max(ret, cand)
    return ret


def sushi(input_case):
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
        n = input_list[cursor][0]
        budget = input_list[cursor][1]
        price_pref_set = input_list[cursor + 1:cursor + 1 + n]
        CACHE = [-1 for j in range(201)]
        print n, budget
        print _sushi(budget, price_pref_set)
        cursor = cursor + n + 1


if __name__ == '__main__':
    input_case = \
        '''2
        6 10000
        2500 7
        3000 9
        4000 10
        5000 12
        10000 20
        15000 1
        6 543975612
        2500 7
        3000 9
        4000 10
        5000 12
        10000 20
        15000 1'''
    sushi(input_case)
