# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        cur = l_result = ListNode(0)

        while l1 and l2:
            cur.val += l1.val + l2.val
            l1 = l1.next
            l2 = l2.next
            if cur.val >= 10:
                cur.val %= 10
                cur.next = ListNode(1)
            else:
                if l1 or l2:
                    cur.next = ListNode(0)

            cur = cur.next

        while l1:
            cur.val += l1.val
            l1 = l1.next
            if cur.val >= 10:
                cur.val %= 10
                cur.next = ListNode(1)
            else:
                if l1:
                    cur.next = ListNode(0)
            cur = cur.next

        while l2:
            cur.val += l2.val
            l2 = l2.next
            if cur.val >= 10:
                cur.val %= 10
                cur.next = ListNode(1)
            else:
                if l2:
                    cur.next = ListNode(0)	
            cur = cur.next

        return l_result