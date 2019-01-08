def match(target, source):
    pos = 0
    while (pos < len(target) and pos < len(source)
           and (target[pos] == '?' or target[pos] == source[pos])):
        pos = pos + 1

    if (pos == len(target)):
        return pos == len(source)

    if (target[pos] == '*'):
        for i in range(pos, len(source) + 1):
            if match(target[pos+1:], source[i:]):
                return True

    return False


def wildcard(input_case):
    input_list = list(
        map(
            lambda x: x.strip(),
            input_case.split('\n')
        )
    )
    case_num = int(input_list[0])
    input_list = input_list[1:]
    case_cursor = 0
    for i in range(case_num):
        target = input_list[case_cursor]
        source_num = int(input_list[case_cursor+1])
        sources = input_list[case_cursor+1+1:case_cursor+1+1+source_num]
        case_cursor = case_cursor + 1 + source_num + 1

        for source in sources:
            if match(target, source):
                print source


if __name__ == '__main__':
    input_case = \
        '''3
        he?p
        3
        help
        heap
        helpp
        *p*
        3
        help
        papa
        hello
        *bb*
        1
        babbbc'''
    wildcard(input_case)
