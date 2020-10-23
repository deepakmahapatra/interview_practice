"""
Problem:
- Given the head of a singly linked list, write a function to determine
  if it contains a cycle.
Approach:
- Have a slow pointer move one step at a time while the fast one move
  2 steps at a time.
- If the linked list has a cycle, the fast pointer will catch the slow one.
Cost:
- O(n) time, O(1) space.
"""


class ListNode:
    def __init__(self, value, next_=None):
        self.value = value
        self.next_ = next_


def cycle_linked_list(list_node: ListNode):
    slow = list_node
    fast = list_node

    while fast and fast.next_:
        slow = slow.next_
        fast = fast.next_.next_

    # // if the fast pointer catches the slow one, there exists a cycle.
        if fast.value == slow.value:
            return True
    return False


if __name__ == '__main__':
    t3 = ListNode(3)
    t2 = ListNode(2, t3)
    t1 = ListNode(1, t2)

    t6 = ListNode(3)
    t5 = ListNode(2, t6)
    t4 = ListNode(1, t5)
    t6.next_ = t4

    print(cycle_linked_list(t1))
    print(cycle_linked_list(t4))
