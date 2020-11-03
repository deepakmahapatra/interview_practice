# Find the maximum width of a binary tree
from btree import Btree, Node


class Solution:
    def max_width(self, root, level):
        if not root:
            return 0
        if level == 1:
            return 1
        if level > 1:
            return self.max_width(root.left, level-1) + self.max_width(root.right, level-1)

    def max_width_without_empty(self, root: Node) -> int:
        queue_ = [root]
        max_width = 0
        level = 1
        while queue_:
            width = self.max_width(root, level)
            queue_ = [child for node in queue_ for child in [node.left, node.right] if child]
            max_width = max(width, max_width)
            level += 1
        return max_width

    def max_width_without_empty_with_ht(self, root: Node) -> int:
        height = self.height_of_tree(root)
        max_width = 0
        for i in range(0, height+1):
            width = self.max_width(root, i)
            max_width = max(width, max_width)
        return max_width

    def height_of_tree(self, node: Node):
        if not node:
            return 0
        l_height = self.height_of_tree(node.left)
        r_height = self.height_of_tree(node.right)
        if l_height > r_height:
            return l_height+1
        return r_height+1

    def max_width_with_empty_in_between(self, root: Node):
        queue = [(1, root)]
        max_width = 0
        while queue:
            max_width = max(max_width, queue[-1][0] - queue[0][0] + 1)
            temp = []
            for position, node in queue:
                for item in enumerate((node.left, node.right), 2 * position):
                    if item[0]:
                        temp.append(item)
            queue = temp
        return max_width
