#
# @lc app=leetcode.cn id=2 lang=python3
#
# [2] 两数相加
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        # r = re = ListNode(0)
        # carry = 0
        # while(l1 or l2):
        #     x = l1.val if l1 else 0
        #     y = l2.val if l2 else 0
        #     s = carry + x + y
        #     carry = s // 10
        #     r.next = ListNode(s % 10)
        #     r = r.next
        #     if(l1 != None):
        #         l1 = l1.next
        #     if(l2 != None):
        #         l2 = l2.next
        # if(carry > 0):
        #     r.next = ListNode(1)
        # return re.next
        def add(a, b, carry):
            if not (a or b):
                return ListNode(1) if carry else None
            a = a if a else ListNode(0)
            b = b if b else ListNode(0)
            val = a.val + b.val + carry
            a.val = val % 10
            carry = val // 10
            a.next = add(a.next, b.next, carry)
            return a
        return add(l1, l2, 0) 
# @lc code=end
