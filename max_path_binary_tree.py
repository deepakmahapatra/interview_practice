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

    def maxPathSum(self, root):
        self.maxPathSumHelper(root)
        return self.current_max

    def maxPathSumHelper(self, node):
        if not node:
            return node
        left = self.maxPathSumHelper(node.left)
        right = self.maxPathSumHelper(node.right)

        left = 0 if not left else (left if left >0 else 0)
        right = 0 if not right else (right if right >0 else 0)
        self.current_max = max(self.current_max, node.val + left + right)
        return max(left, right) + node.val

