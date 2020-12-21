def detectCycle(A):
    slow = A
    fast = A
    while slow and fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            break
    if slow != fast: return None
    slow = A
    while slow != fast:
        slow = slow.next
        fast = fast.next
    return slow
