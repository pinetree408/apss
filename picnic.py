def recursive(source, target, log, result, student_num):
    if len(target) == 0 and len(source) == 0:
        log.sort()
        if log not in result:
            result.append(log)
        return

    for pair in source:
        new_log = log[:]
        pair.sort()
        new_log.append(pair)
        new_pair_list = source[:]
        for comp in source[:]:
            if pair[0] in comp or pair[1] in comp:
                new_pair_list.remove(comp)
        new_target = target[:]
        new_target.remove(pair[0])
        new_target.remove(pair[1])
        recursive(new_pair_list, new_target, new_log, result, student_num)


def picnic(input_case):
    input_list = list(
        map(
            lambda x: [int(i) for i in x.strip().split(' ')],
            input_case.split('\n')
        )
    )
    case_num = input_list[0][0]
    input_list = input_list[1:]
    for i in range(case_num):
        test_case = input_list[i*2:(i+1)*2]
        student_num = test_case[0][0]
        friend_pair_num = test_case[0][1]
        pair_list = [
            test_case[1][i*2:(i+1)*2] for i in range(friend_pair_num)
        ]

        result = []
        student_num_list = [j for j in range(student_num)]
        recursive(pair_list, student_num_list, [], result, student_num)
        print len(result)


if __name__ == '__main__':
    input_case = \
        '''3
        2 1
        0 1
        4 6
        0 1 1 2 2 3 3 0 0 2 1 3
        6 10
        0 1 0 2 1 2 1 3 1 4 2 3 2 4 3 4 3 5 4 5'''
    picnic(input_case)
