class Node:

    def __init__(self, data):

        self.left = None
        self.right = None
        self.data = data


class Btree:

    def __init__(self):
        self.head = None

    def insert(self, head, data):
        # Compare the new value with the parent node
        if head.data:
            if data < head.data:
                if not head.left:
                    head.left = Node(data)
                else:
                    self.insert(head.left, data)
            elif data > head.data:
                if not head.right:
                    head.right = Node(data)
                else:
                    self.insert(head.right, data)
        else:
            head.data = data

    def lookup(self, head, data):
        if not head:
            return None
        if head.data == data:
            return head.data
        if data <= head.data:
            return self.lookup(head.left, data)
        else:
            return self.lookup(head.right, data)

    def get_min_value(self, head):
        if not head:
            return None
        if not head.left:
            return head.data
        return self.get_min_value(head.left)

    def get_max_depth(self, head):
        if not head:
            return 0
        if not head.left and not head.right:
            return 0
        left_max = 1 + self.get_max_depth(head.left)
        right_max = 1 + self.get_max_depth(head.right)
        return max(left_max, right_max)

    def mirror_binary_tree(self, head):
        if not head:
            return
        self.mirror_binary_tree(head.left)
        self.mirror_binary_tree(head.right)

        temp = head.left
        head.left = head.right
        head.right = temp

    def structurally_unique_count_trees(self, num_nodes):
        """
        finds the number of structurally unique btrees possible
        :param: num_nodes
        :return:
        """
        if num_nodes <= 1:
            return 1
        sum = 0
        for i in range(num_nodes+1):
            count_left_trees = self.structurally_unique_count_trees(i-1)
            count_right_trees = self.structurally_unique_count_trees(num_nodes-1)

            sum = sum + (count_left_trees * count_right_trees) # number of subtrees possible with i as the root
        return sum

    def print_nodes_in_range(self, node, low, high):
        """
        returns all nodes within a range in a binary search tree can be zero as well
        check every node to see if value is in between the range
        :param node:
        :param high:
        :param low:
        :return:
        """
        if not node:
            return
        if low <= node.data:
            self.print_nodes_in_range(node.left, low, high)
        if low <= node.data <= high:
            print(node.data)
        if high > node.data:
            self.print_nodes_in_range(node.right, low, high)


    def is_bst(self, node, min=float('-inf'), max=float('inf')):
        """
        check if btree is a binary search tree

        :param node:
        :param min: Initially interger min
        :param max: Initially integer max
        :return:
        """
        if not node:
            return True
        if max < node.data or node.data <= min:
            return False
        return self.is_bst(node.left, min, node.data) and self.is_bst(node.right, node.data, max)

    def sum_path_from_root(self, node, sum):
        if not node.left and not node.right:
            return sum == node.data
        subsum = sum - node.data

        if node.left:
            has_path_sum = self.sum_path_from_root(node.left, subsum)
            if has_path_sum:
                return True
        if node.right:
            has_path_sum = self.sum_path_from_root(node.right, subsum)
            if has_path_sum:
                return True
        return False

    def print_all_path_root_to_leaf(self, node, path_list):
        if not node:
            return
        path_list.append(node)
        self.print_all_path_root_to_leaf(node.left, path_list)
        self.print_all_path_root_to_leaf(node.right, path_list)
        if not node.left and not node.right:
            print(path_list)
        path_list.remove(node)

    def least_common_ancestor(self, node, node1, node2):
        if not node:
            return None
        if node == node1 or node == node2:
            return node
        left_lca = self.least_common_ancestor(node.left, node1, node2)
        right_lca = self.least_common_ancestor(node.right, node1, node2)

        if left_lca and right_lca:
            return node
        if left_lca:
            return left_lca
        return right_lca

    # @param A : root node of tree
    # @param B : integer
    # @param C : integer
    # @return an integer

    def lca(self, A, B, C):
        """
        if not sure about B's and C's presence in the tree
        :param A:
        :param B:
        :param C:
        :return:
        """
        v = [False, False]

        res = self.lca_helper(A, B, C, v)
        if res != None and v[0] and v[1] or (v[1] and self.find(A, B)) or (v[0] and self.find(A, C)):
            return res
        return -1

    def find(self, root, k):
        # Base Case
        if root is None:
            return False

        # If key is present at root, or if left subtree or right
        # subtree , return true
        if (root.val == k or self.find(root.left, k) or
                self.find(root.right, k)):
            return True
        # Else return false
        return False

    def lca_helper(self, A, B, C, v):
        if not A:
            return None
        if A.val == B:
            v[0] = True
            return A.val
        if A.val == C:
            v[1] = True
            return A.val
        left_lca = self.lca_helper(A.left, B, C, v)
        right_lca = self.lca_helper(A.right, B, C, v)
        if left_lca != None and right_lca != None:
            return A.val
        if left_lca != None:
            return left_lca
        if right_lca != None:
            return right_lca
        return None

    def deepest_leaf_sum(self, node):
        if not node:
            return 0
        queue = [node]
        previous_level = []
        while queue:
            previous_level, queue = queue, [child for prev in queue for child in [prev.left, prev.right] if child]
        return sum(node.val for node in previous_level)


    # Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param A : root node of tree
    # @param B : integer
    # @return an integer
    def t2Sum(self, A, B):
        list_ = []

        def inorder_helper(A, list_):
            if not A:
                return
            inorder_helper(A.left, list_)
            list_.append(A.val)
            inorder_helper(A.right, list_)

        inorder_helper(A, list_)
        left, right = 0, len(list_) - 1
        while left < right:
            if list_[left] + list_[right] == B:
                return 1
            if list_[left] + list_[right] < B:
                left += 1
            else:
                right -= 1
        return 0

    # @param A : root node of tree
    # @param B : integer
    # @return an integer
    def kthsmallest(self, A, B):
        """
        Given a binary search tree, write a function to find the kth smallest element in the tree.

        Example :

        Input :
          2
         / \
        1   3

        and k = 2

        Return : 2

        As 2 is the second smallest element in the tree.
        :param A:
        :param B:
        :return:
        """
        stack = [A]
        counter = 0
        while stack:
            node = stack.pop()
            if not node.left and not node.right:
                counter += 1
                if counter == B:
                    return node.val
            else:
                if node.right:
                    stack.append(node.right)
                    node.right = None
                stack.append(node)
                if node.left:
                    stack.append(node.left)
                    node.left = None

    def kthsmallest_recursion(self, A, B):
        self.B = B
        def preorder(A):
            if not A:
                return
            res = preorder(A.left)
            if res:
                return res.val
            if self.B == 1:
                return A.val
            self.B -= 1
            return preorder(A.right)

        return preorder(A)

    def flatten_tree(self, A):
        """
        Given a binary tree, flatten it to a linked list in-place.
        Example :
        Given


                 1
                / \
               2   5
              / \   \
             3   4   6
        The flattened tree should look like:

           1
            \
             2
              \
               3
                \
                 4
                  \
                   5
                    \
                     6
        Note that the left child of all nodes should be NULL.

        If you notice carefully in the flattened tree, each node’s right child points to the next node of a pre-order traversal.

        Now, if a node does not have left node, then our problem reduces to solving it for the node->right.
        If it does, then the next element in the preorder traversal is the immediate left child. But if we make the immediate left child as the right child of the node, then the right subtree will be lost.
        So we figure out where the right subtree should go. In the preorder traversal, the right subtree comes right
        after the rightmost element in the left subtree.
        So we figure out the rightmost element in the left subtree, and
        attach the right subtree as its right child. We make the left child as the right child now and move on to the next node.
        :param A:
        :return:
        """
        current = A
        stack = []
        while current or stack:
            if current.right:
                stack.append(current.right)
            if not current.left and stack:
                current.left = stack.pop()
            if current.left:
                current.right = current.left
            current.left = None
            current = current.right
        return A

    def buildTree(self, A, B):
        """
        Given inorder and postorder traversal of a tree, construct the binary tree.

         Note: You may assume that duplicates do not exist in the tree.
        Example :

        Input :
                Inorder : [2, 1, 3]
                Postorder : [2, 3, 1]

        Return :
            1
           / \
          2   3
        :param A:
        :param B:
        :return:
        """
        if not A or not B:
            return
        rootpos = A.index(B[-1])
        root = TreeNode(B[-1])
        root.left = self.buildTree(A[:rootpos], B[:rootpos])
        root.right = self.buildTree(A[rootpos + 1:], B[rootpos:-1])
        return root

    def is_bst_from_preorder(self, items):
        """
        The idea is to use a stack. This problem is similar to Next (or closest) Greater Element problem.
        Here we find the next greater element and after finding next greater, if we find a smaller element, then return false.

        Create an empty stack.
        Initialize root as INT_MIN.
        Do following for every element pre[i]
        If pre[i] is smaller than current root, return false.
        Keep removing elements from stack while pre[i] is greater
        then stack top. Make the last removed item as new root (to
        be compared next).
        At this point, pre[i] is greater than the removed root
        (That is why if we see a smaller element in step a), we
        return false)
        push pre[i] to stack (All elements in stack are in decreasing order)
        :param items:
        :return:
        """
        stack =[]
        node_val = float('-inf')
        for item in items:
            if item < node_val:
                return 0
            if stack and stack[-1] < item:
                node_val = stack.pop()
            stack.append(item)
        return 1

    def merge_two_btree(self, A, B):
        # @param A : root node of tree
        # @param B : root node of tree
        # @return the root node in the tree
        """
        Problem Description
        Given two Binary Trees A and B, you need to merge them in a single binary tree.
        The merge rule is that if two nodes overlap, then sum of node values is the new value of the merged node.
        Otherwise, the non-null node will be used as the node of new tree.
        Problem Constraints
        1 <= Number of Nodes in A , B <= 105
        Input Format
        First argument is an pointer to the root of binary tree A.
        Second argument is an pointer to the root of binary tree B.
        Output Format
        Return a pointer to the root of new binary tree.
        Example Input
        Input 1:
         A =   2

              / \

             1   4

            /

           5


        B =   3
              / \
              6  1
              \   \
               2   7

        Input 2:

         A =   12

              / \

             11  14


        B =   3
              / \
              6  1



        Example Output
        Output 1:

             5
            / \
           7   5
          / \   \
         5   2   7
        Output 2:

           15
          / \
         17  15
        :param A:
        :param B:
        :return:
        """
        if not A:
            return B
        if not B:
            return A
        A.val += B.val
        A.left = self.merge_two_btree(A.left, B.left)
        A.right = self.merge_two_btree(A.right, B.right)
        return A

    def remove_half_nodes(self, A):
        """
        Problem Description

        Given a binary tree A with N nodes.

        You have to remove all the half nodes and return the final binary tree.

        NOTE:

        Half nodes are nodes which have only one child.
        Leaves should not be touched as they have both children as NULL.


        Problem Constraints
        1 <= N <= 105



        Input Format
        First and only argument is an pointer to the root of binary tree A.



        Output Format
        Return a pointer to the root of the new binary tree.



        Example Input
        Input 1:

                   1
                 /   \
                2     3
               /
              4

        Input 2:

                    1
                  /   \
                 2     3
                / \     \
               4   5     6


        Example Output
        Output 1:

                   1
                 /    \
                4      3
        Output 2:

                    1
                  /   \
                 2     6
                / \

               4   5



        Example Explanation
        Explanation 1:

         The only half node present in the tree is 2 so we will remove this node.
        Explanation 2:

         The only half node present in the tree is 3 so we will remove this node.
        """
        if not A:
            return
        A.left = self.remove_half_nodes(A.left)
        A.right = self.remove_half_nodes(A.right)
        if bool(A.left) == bool(A.right):
            return A
        if not A.left:
            return A.right
        return A.left

    def max_binary_tree(self, nums):
        """
        You are given an integer array nums with no duplicates. A maximum binary tree can be built recursively from nums using the following algorithm:

        Create a root node whose value is the maximum value in nums.
        Recursively build the left subtree on the subarray prefix to the left of the maximum value.
        Recursively build the right subtree on the subarray suffix to the right of the maximum value.
        Return the maximum binary tree built from nums.
        :param nums:
        :return:
        """
        if not nums:
            return
        stack = []
        for num in nums:
            node = TreeNode(num)
            while stack and stack[-1].val < num:
                node.left = stack.pop()
            if stack:
                stack[-1].right = node

            stack.append(node)
        return stack[0]

    def bst_from_preorder(self, items):
        return self.bst_from_preorder_helper(items, float('-inf'))

    def bst_from_preorder_helper(self, items, bound):
        if not items or items[-1] > bound:
            return
        node = TreeNode(items.pop())
        node.left = self.bst_from_preorder_helper(items, node.val)
        node.right = self.bst_from_preorder_helper(items, bound)
        return node
