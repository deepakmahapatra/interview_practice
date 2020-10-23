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
            return  0
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
