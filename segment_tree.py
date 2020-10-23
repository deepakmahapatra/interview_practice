from math import inf

MAX_VALUE = float(inf)


def construct_segment_tree(segtree, a, n):
    # assign values to leaves of
    # the segment tree
    for i in range(n):
        segtree[n + i] = a[i]

        # assign values to remaining nodes
    # to compute minimum in a given range
    for i in range(n - 1, 0, -1):
        segtree[i] = min(segtree[2 * i],
                         segtree[2 * i + 1])



def range_query(segtree, left, right, n):
    left += n
    right += n

    """ Basically the left and right indices  
        will move towards right and left respectively  
        and with every each next higher level and  
        compute the minimum at each height change  
        the index to leaf node first """
    mi = 1e9  # initialize minimum to a very high value
    while (left < right):
        if (left & 1):  # if left index in odd
            mi = min(mi, segtree[left])
            left = left + 1
        if (right & 1):  # if right index in odd
            right -= 1
            mi = min(mi, segtree[right])

            # move to the next higher level
        left = left // 2
        right = right // 2
    return mi


if __name__ == '__main__':

    input = [-1, 2, 4, 0]
    tree = [0] * (2 * len(input))
    construct_segment_tree(tree, input, len(input))
    print(tree)
    print(range_query(tree, 1, 2, 4))


