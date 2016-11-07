# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        carry = 0
        cur = None
        while l1 or l2 or carry:
            val = (l1.val if l1 else 0) + (l2.val if l2 else 0) + carry
            carry = val//10
            val %= 10
            if cur is None:
                res = ListNode(val)
                cur = res
            else:
                cur.next = ListNode(val)
                cur = cur.next
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        return res
        
