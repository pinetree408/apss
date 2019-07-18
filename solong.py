class TrieNode(object):
    def __init__(self):
        self.terminal = -1
        self.first = -1
        self.children = [0 for i in range(26)]

    def insert(self, key, _id):
        if self.first == -1:
            self.first = _id
        if len(key) == 0:
            self.terminal = _id
        else:
            next_key = ord(key[0])-ord('A')
            if self.children[next_key] == 0:
                self.children[next_key] = TrieNode()
            self.children[next_key].insert(key[1:], _id)

    def find(self, key):
        if len(key) == 0:
            return self
        next_key = ord(key[0])-ord('A')
        if self.children[next_key] == 0:
            return 0
        return self.children[next_key].find(key[1:])

    def type(self, key, _id):
        if len(key) == 0:
            return 0
        if self.first == _id:
            return 1
        next_key = ord(key[0])-ord('A')
        return 1+self.children[next_key].type(key[1:], _id)


def count_keys(trie, word):
    node = trie.find(word)
    if node == 0 or node.terminal == -1:
        return len(word)
    return trie.type(word, node.terminal)


def solong(input_case):
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
        words = []
        for item in input_list[start+1:start+1+n]:
            words.append([item[0], int(item[1])])
        words = sorted(words, key=lambda x: x[0])
        words = sorted(words, key=lambda x: x[1], reverse=True)
        trie = TrieNode()
        for j, word in enumerate(words):
            trie.insert(word[0], j)
        trie.first = -1
        targets = input_list[start+1+n]
        result = m-1
        for target in targets:
            result = result+count_keys(trie, target)
        print result
        case_start = start+1+n+1


if __name__ == '__main__':
    input_case = \
        '''2
        7 8
        ALL 4
        AND 3
        FISH 8
        FOR 6
        SO 4
        THANKS 9
        THE 9
        SO LONG AND THANKS FOR ALL THE FISH
        7 8
        ALL 4
        AND 5
        FISH 3
        FOR 6
        SO 8
        THANKS 1
        THE 2
        SO LONG AND THANKS FOR ALL THE FISH'''
    solong(input_case)
