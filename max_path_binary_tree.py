# Given a non-empty binary tree, find the maximum path sum.
#
# For this problem, a path is defined as any sequence of nodes from some starting node to any node in the tree along the parent-child connections. The path must contain at least one node and does not need to go through the root.
#
# Example 1:
#
# Input: [1,2,3]
#
#        1
#       / \
#      2   3
#
# Output: 6
# Example 2:
#
# Input: [-10,9,20,null,null,15,7]
#
#    -10
#    / \
#   9  20
#     /  \
#    15   7
#
# Output: 42


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    current_max = float('-inf')

    def max_path_sum(self, root):
        self.max_path_sum_helper(root)
        return self.current_max

    def max_path_sum_helper(self, node):
        if not node:
            return node
        left = self.max_path_sum_helper(node.left)
        right = self.max_path_sum_helper(node.right)

        left = 0 if not left else (left if left > 0 else 0)
        right = 0 if not right else (right if right > 0 else 0)
        self.current_max = max(self.current_max, node.val + left + right)
        return max(left, right) + node.val

    def least_root_to_leaf_path(self, node):
        queue = [node]
        while queue:
            queue = [child for node in queue for child in [node.left, node.right] if child]

    def bst_from_preorder(self, preorder: list) -> TreeNode:
        root = TreeNode(preorder[0])
        stack = [root]
        for value in preorder[1:]:
            if value < stack[-1].val:
                stack[-1].left = TreeNode(value)
                stack.append(stack[-1].left)
            else:
                while stack and stack[-1].val < value:
                    last = stack.pop()
                last.right = TreeNode(value)
                stack.append(last.right)
        return root
