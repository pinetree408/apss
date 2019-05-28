BEST = 0


def search(can_eat, eaters, edible, chosen):
    global BEST
    if chosen >= BEST:
        return
    first = 0
    while first < len(can_eat) and edible[first] > 0:
        first = first + 1
    if first == len(can_eat):
        BEST = chosen
        return
    for i in range(len(can_eat[first])):
        food = can_eat[first][i]
        for j in range(len(eaters[food])):
            edible[eaters[food][j]] = edible[eaters[food][j]] + 1
        search(can_eat, eaters, edible, chosen+1)
        for j in range(len(eaters[food])):
            edible[eaters[food][j]] = edible[eaters[food][j]] - 1


def allergy(input_case):
    global BEST
    input_list = list(
        map(
            lambda x: x.strip(),
            input_case.split('\n')
        )
    )
    case_num = int(input_list[0])
    input_list = input_list[1:]
    case_start = 0
    for i in range(case_num):
        start = case_start
        party_info = input_list[start].split(' ')
        friend_num = int(party_info[0])
        food_num = int(party_info[1])
        friend_list = input_list[start+1].split(' ')
        food_info_list = []
        for j in range(food_num):
            food_info_list.append(input_list[start+1+j+1].split(' ')[1:])
        can_eat = [[] for k in range(friend_num)]
        for idx_friend, friend in enumerate(friend_list):
            for idx_food_info, food_info in enumerate(food_info_list):
                if friend in food_info:
                    can_eat[idx_friend].append(idx_food_info)
        eaters = [[] for k in range(food_num)]
        for idx_food_info, food_info in enumerate(food_info_list):
            for idx_friend, friend in enumerate(friend_list):
                if friend in food_info:
                    eaters[idx_food_info].append(idx_friend)
        BEST = food_num
        edible = [0 for k in range(friend_num)]
        chosen = 0
        search(can_eat, eaters, edible, chosen)
        print BEST
        case_start = start + 1 + food_num + 1


if __name__ == '__main__':
    input_case = \
        '''2
        4 6
        cl bom dara minzy
        2 dara minzy
        2 cl minzy
        2 cl dara
        1 cl
        2 bom dara
        2 bom minzy
        10 7
        a b c d e f g h i j
        6 a c d h i j
        3 a d i
        7 a c f g h i j
        3 b d g
        5 b c f h i
        4 b e g j
        5 b c g h i'''
    allergy(input_case)
