cache = [[]]
counter = 0


class TrieNode(object):
    def __init__(self):
        self.no = None
        self.terminal = -1
        self.children = [None for i in range(26)]
        self.next = [None for i in range(26)]
        self.fail = None
        self.output = []

    def insert(self, key, _id):
        if len(key) == 0:
            self.terminal = _id
        else:
            next_key = ord(key[0])-ord('a')
            if self.children[next_key] is None:
                self.children[next_key] = TrieNode()
            self.children[next_key].insert(key[1:], _id)


def compute_fail_func(root):
    q = []
    root.fail = root
    q.append(root)
    while len(q) != 0:
        here = q[0]
        q.pop(0)
        for edge in range(26):
            child = here.children[edge]
            if child is None:
                continue
            if here == root:
                child.fail = root
            else:
                t = here.fail
                while (t != root) and (t.children[edge] is None):
                    t = t.fail
                if t.children[edge] is not None:
                    t = t.children[edge]
                child.fail = t
            child.output = list(child.fail.output)
            if child.terminal != -1:
                child.output.append(child.terminal)
            q.append(child)


def solve(trie, length):
    global cache
    if len(trie.output) > 0:
        return 0
    if length == 0:
        return 1
    if cache[length][trie.no] != -1:
        return cache[length][trie.no]
    cache[length][trie.no] = 0
    for i in range(26):
        cache[length][trie.no] =\
            (cache[length][trie.no]+solve(
                trie.next[i], length-1
            )) % 10007
    return cache[length][trie.no]


def compute_transition(here):
    global counter
    here.no = counter
    counter = counter+1
    for c in range(26):
        next_node = here
        while (next_node != next_node.fail) and\
                (next_node.children[c] is None):
            next_node = next_node.fail
        if next_node.children[c] is not None:
            next_node = next_node.children[c]
        here.next[c] = next_node
        if here.children[c] is not None:
            compute_transition(here.children[c])


def nh(input_case):
    global cache, counter
    input_list = list(
        map(
            lambda x: [i for i in x.strip().split(' ')],
            input_case.split('\n')
        )
    )
    case_num = int(input_list[0][0])
    input_list = input_list[1:]

    case_start = 0
    for i in range(case_num):
        start = case_start
        n = int(input_list[start][0])
        m = int(input_list[start][1])
        patterns = input_list[start+1:start+1+m]
        cache = [
            [-1 for j in range(1001)] for k in range(101)
        ]
        trie = TrieNode()
        for t in range(m):
            trie.insert(patterns[t][0], t)
        compute_fail_func(trie)
        counter = 0
        compute_transition(trie)
        print solve(trie, n)
        case_start = start+1+m


if __name__ == '__main__':
    input_case = \
        '''3
        2 2
        rm
        dd
        4 4
        a
        b
        c
        d
        100 4
        aa
        ba
        ab
        cd'''
    nh(input_case)
