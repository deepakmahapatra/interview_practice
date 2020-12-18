# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def list_to_bst(A):
    """
    Given a singly linked list where elements are sorted in ascending order, convert it to a height balanced BST.

     A height balanced BST : a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of every node never differ by more than 1.
    Example :


    Given A : 1 -> 2 -> 3
    A height balanced BST  :

          2
        /   \
       1     3
    """
    # @param A : head node of linked list
    # @return the root node in the tree
    l = []
    while A:
        l.append(A.val)
        A = A.next
    return sorted_list_helper(l)


def sorted_list_helper(l):
    if not l:
        return
    i = len(l) // 2
    node = TreeNode(l[i])
    node.left = sorted_list_helper(l[:i])
    node.right = sorted_list_helper(l[i + 1:])
    return node

