import sys
no_serial = []
serial_no = []
loc_in_trip = []
depth = []
next_serial = 0


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


def traverse(here, d, trip, child):
    global next_serial, no_serial, serial_no, depth, loc_in_trip
    no_serial[here] = next_serial
    serial_no[next_serial] = here
    next_serial = next_serial+1
    depth[here] = d
    loc_in_trip[here] = len(trip)
    trip.append(no_serial[here])
    if here in child:
        for i in range(len(child[here])):
            traverse(child[here][i], d+1, trip, child)
            trip.append(no_serial[here])


def prepare_RMQ(child):
    global next_serial
    next_serial = 0
    trip = []
    traverse(0, 0, trip, child)
    return RMQ(trip)


def distance(rmq, u, v):
    global serial_no, loc_in_trip, depth
    lu = loc_in_trip[u]
    lv = loc_in_trip[v]
    if lu > lv:
        lu, lv = lv, lu
    lca = serial_no[rmq.query(lu, lv)]
    return depth[u] + depth[v] - 2*depth[lca]


def familytree(input_case):
    global next_serial, no_serial, serial_no, loc_in_trip, depth
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
        n = input_list[start][0]
        q = input_list[start][1]
        people = input_list[start+1]
        child = {}
        for j in range(n-1):
            if people[j] in child:
                child[people[j]].append(j+1)
            else:
                child[people[j]] = [j+1]
        target_list = input_list[start+1+1:start+1+1+q]
        no_serial = [0 for i in range(n)]
        serial_no = [0 for i in range(n)]
        loc_in_trip = [0 for i in range(n)]
        depth = [0 for i in range(n)]
        rmq = prepare_RMQ(child)
        for target in target_list:
            print distance(rmq, target[0], target[1])
        case_start = start+1+1+q


if __name__ == '__main__':
    input_case = \
        '''1
        13 5
        0 1 1 3 3 0 6 0 8 9 9 8
        2 7
        10 11
        4 11
        7 7
        10 0'''
    familytree(input_case)
