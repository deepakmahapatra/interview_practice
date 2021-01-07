from queue import PriorityQueue
from typing import List

from linked_list_cycle import ListNode


def merge_k_lists(lists: List[ListNode]) -> ListNode:
    dummy = ListNode(None)
    curr = dummy
    q = PriorityQueue()
    for idx, node in enumerate(lists):
        if node:
            q.put((node.value, idx, node))
    while q.qsize() > 0:
        item = q.get()
        curr.next, idx = item[2], item[1]
        curr = curr.next
        if curr.next:
            q.put((curr.next.val, idx, curr.next))
    return dummy.next_

