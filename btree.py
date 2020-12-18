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

    def print_nodes_in_range(self, node, high, low):
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
        if max < node.data <= min:
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
            If it does, then the next element in the preorder traversal is the immediate left child. But if we make the immediate left child as the right child of the node, then the right subtree will be lost. So we figure out where the right subtree should go. In the preorder traversal, the right subtree comes right after the rightmost element in the left subtree.
            So we figure out the rightmost element in the left subtree, and attach the right subtree as its right child. We make the left child as the right child now and move on to the next node.
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
