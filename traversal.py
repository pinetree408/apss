def print_post_order(preorder, inorder):
    n = len(preorder)
    if n == 0:
        return
    root = preorder[0]
    left = inorder.index(root)
    print_post_order(preorder[1:left+1], inorder[:left])
    print_post_order(preorder[left+1:n], inorder[left+1:n])
    print root


def traversal(input_case):
    input_list = list(
        map(
            lambda x: [int(i) for i in x.strip().split(' ')],
            input_case.split('\n')
        )
    )
    case_num = int(input_list[0][0])
    input_list = input_list[1:]

    for i in range(case_num):
        preorder = input_list[i*2+1]
        inorder = input_list[i*2+2]
        print_post_order(preorder, inorder)


if __name__ == '__main__':
    input_case = \
        '''1
        7
        27 16 9 12 54 36 72
        9 12 16 27 36 54 72'''
    traversal(input_case)
