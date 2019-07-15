class FenwickTree(object):
    def __init__(self, n):
        self.tree = [0 for i in range(n+1)]

    def sum(self, pos):
        pos = pos+1
        result = 0
        while pos > 0:
            result = result+self.tree[pos]
            pos = pos & (pos-1)
        return result

    def add(self, pos, val):
        pos = pos+1
        while pos < len(self.tree):
            self.tree[pos] = self.tree[pos]+val
            pos = pos+(pos & -pos)


def count_moves(n, a_list):
    tree = FenwickTree(1000000)
    result = 0
    for i in range(n):
        result = result+tree.sum(999999)-tree.sum(a_list[i])
        tree.add(a_list[i], 1)
    return result


def measuretime(input_case):
    input_list = list(
        map(
            lambda x: [int(i) for i in x.strip().split(' ')],
            input_case.split('\n')
        )
    )
    case_num = int(input_list[0][0])
    input_list = input_list[1:]

    for i in range(case_num):
        n = input_list[i*2][0]
        a_list = input_list[i*2+1]
        print count_moves(n, a_list)


if __name__ == '__main__':
    input_case = \
        '''2
        5
        5 1 4 3 2
        10
        7 8 6 6 1 9 4 4 3 10'''
    measuretime(input_case)
