# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


def hasCycle(self, head):
    """
    :type head: ListNode
    :rtype: bool
    """
    fast = slow = head
    while slow and fast and fast.next:
        slow.next
        fast.next.next
        if slow == fast:
            return True
    return False

head = [3,2,0,-4]
result = hasCycle(head)