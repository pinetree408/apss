def fanmetting(input_case):
    input_list = list(
        map(
            lambda x: x.strip(),
            input_case.split('\n')
        )
    )
    case_num = int(input_list[0])
    input_list = input_list[1:]
    for i in range(case_num):
        singer_list = list(input_list[i*2])
        fan_list = list(input_list[i*2+1])
        counter = 0
        for j in range(0, len(fan_list) - len(singer_list) + 1):
            target_fan_list = fan_list[j:j+len(singer_list)]
            hand_shake_flag = False
            for f, s in zip(target_fan_list, singer_list):
                if f == 'M' and s == 'M':
                    hand_shake_flag = True
                    break
            if not hand_shake_flag:
                counter += 1
        print counter


if __name__ == '__main__':
    input_case = \
        '''4
        FFFMMM
        MMMFFF
        FFFFF
        FFFFFFFFFF
        FFFFM
        FFFFFMMMMF
        MFMFMFFFMMMFMF
        MMFFFFFMFFFMFFFFFFMFFFMFFFFMFMMFFFFFFF'''
    fanmetting(input_case)
