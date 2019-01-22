CACHE = [[]]


def pack(capacity, item, volume, need):
    global CACHE
    if item == len(volume):
        return 0
    if CACHE[capacity][item] != -1:
        return CACHE[capacity][item]
    CACHE[capacity][item] = pack(capacity, item + 1, volume, need)
    if capacity >= volume[item]:
        CACHE[capacity][item] = max(
            CACHE[capacity][item],
            pack(
                capacity - volume[item], item + 1,
                volume, need) + need[item]
        )
    return CACHE[capacity][item]


def reconstruct(capacity, item, volume, need, name, picked):
    if item == len(volume):
        return
    if pack(capacity, item, volume, need) ==\
            pack(capacity, item + 1, volume, need):
        reconstruct(capacity, item + 1, volume, need, name, picked)
    else:
        picked.append(name[item])
        reconstruct(
            capacity - volume[item], item + 1, volume, need, name, picked)


def packing(input_case):
    global CACHE
    input_list = list(
        map(
            lambda x: [str(i) for i in x.strip().split(' ')],
            input_case.split('\n')
        )
    )
    case_num = int(input_list[0][0])
    input_list = input_list[1:]
    cursor = 0
    for i in range(case_num):
        item_num = int(input_list[cursor][0])
        capacity = int(input_list[cursor][1])
        name = []
        volume = []
        need = []
        CACHE = [[-1 for j in range(item_num)] for i in range(capacity+1)]
        for j in range(item_num):
            item = input_list[cursor + 1 + j]
            name.append(item[0])
            volume.append(int(item[1]))
            need.append(int(item[2]))
        result = []
        total = pack(capacity, 0, volume, need)
        reconstruct(capacity, 0, volume, need, name, result)
        print total, len(result)
        for item in result:
            print item
        cursor = 1 + item_num


if __name__ == '__main__':
    input_case = \
        '''2
        6 10
        laptop 4 7
        camera 2 10
        xbox 6 6
        grinder 4 7
        dumbell 2 5
        encyclopedia 10 4
        6 17
        laptop 4 7
        camera 2 10
        xbox 6 6
        grinder 4 7
        dumbell 2 5
        encyclopedia 10 4'''
    packing(input_case)
