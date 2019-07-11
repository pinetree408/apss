import sys


class RMQ(object):
    def __init__(self, target):
        self.n = len(target)
        self.range_min = [0 for i in range(self.n*4)]
        self.init(target, 0, self.n-1, 1)

    def init(self, target, left, right, node):
        if left == right:
            self.range_min[node] = target[left]
            return self.range_min[node]
        mid = (left+right)/2
        left_min = self.init(target, left, mid, node*2)
        right_min = self.init(target, mid+1, right, node*2+1)
        self.range_min[node] = min(left_min, right_min)
        return self.range_min[node]

    def _query(self, left, right, node, node_left, node_right):
        if right < node_left or left > node_right:
            return sys.maxint
        if left <= node_left and right >= node_right:
            return self.range_min[node]
        mid = (node_left+node_right)/2
        ret = min(
            self._query(left, right, node*2, node_left, mid),
            self._query(left, right, node*2+1, mid+1, node_right)
        )
        return ret

    def query(self, left, right):
        return self._query(left, right, 1, 0, self.n-1)

    def _update(self, index, new_value, node, node_left, node_right):
        if index < node_left or index > node_right:
            return self.range_min[node]
        if node_left == node_right:
            self.range_min[node] = new_value
            return self.range_min[node]
        mid = (node_left+node_right)/2
        ret = min(
            self._update(index, new_value, node*2, node_left, mid),
            self._update(index, new_value, node*2+1, mid+1, node_right)
        )
        return ret

    def update(self, index, new_value):
        return self._update(index, new_value, 1, 0, self.n-1)


def mordor(input_case):
    input_list = list(
        map(
            lambda x: [int(i) for i in x.strip().split(' ')],
            input_case.split('\n')
        )
    )
    case_num = int(input_list[0][0])
    input_list = input_list[1:]

    case_start = 0
    for i in range(case_num):
        start = case_start
        q = input_list[start][1]
        height_list = input_list[start+1]
        minus_height_list = [-height for height in height_list]

        rmq = RMQ(height_list)
        minus_rmq = RMQ(minus_height_list)

        path_list = input_list[start+1+1:start+1+1+q]
        for path in path_list:
            low = rmq.query(path[0], path[1])
            high = abs(minus_rmq.query(path[0], path[1]))
            print high-low
        case_start = start+1+1+q


if __name__ == '__main__':
    input_case = \
        '''2
        3 1
        1 2 3
        0 2
        10 4
        3 9 5 6 10 8 7 1 2 4
        1 6
        4 7
        9 9
        5 8'''
    mordor(input_case)
