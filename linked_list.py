from linked_list_cycle import ListNode


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


def is_palindrome(head):
    rev = None
    slow = fast = head
    while fast and fast.next:
        fast = fast.next.next
        rev, rev.next, slow = slow, rev, slow.next
    if fast:
        slow = slow.next
    while rev and rev.val == slow.val:
        slow = slow.next
        rev = rev.next
    return not rev


def remove_zero_sum(link):
    dummy = ListNode(None)
    dummy.next = link

    cumulative_sum = 0
    hashmap = {cumulative_sum: dummy}
    while link:
        cumulative_sum += link.val

        if cumulative_sum in hashmap:
            popping_index = hashmap[cumulative_sum].next_
            sum = cumulative_sum
            while popping_index != link:
                sum += popping_index.val
                del hashmap[sum]
                popping_index = popping_index.next_
            hashmap[cumulative_sum].next_ = link.next_
        else:
            hashmap[cumulative_sum] = link
        link = link.next
    return dummy.next_
