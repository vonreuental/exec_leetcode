#
# @lc app=leetcode.cn id=141 lang=python3
#
# [141] 环形链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        # 快慢指针
        # if head is None or head.next is None:
        #     return False
        # slow = head
        # fast = head.next
        # while slow != fast:
        #     if fast is None or fast.next is None:
        #         return False
        #     slow = slow.next
        #     fast = fast.next.next
        # return True
        if not head:
            return head
        m = []
        while head:
            if head in m:
                return True
            m.append(head)
            head = head.next
        return False
# @lc code=end

