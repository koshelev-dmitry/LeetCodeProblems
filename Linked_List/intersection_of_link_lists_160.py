"""
Write a program to find the node at which the intersection of two singly linked lists begins.
Notes:
    If the two linked lists have no intersection at all, return null.
    The linked lists must retain their original structure after the function returns.
    You may assume there are no cycles anywhere in the entire linked structure.
    Your code should preferably run in O(n) time and use only O(1) memory.


My solution is an alternative to the LeetCode, with the same performance, but tones of codding 
Runtime: 304 ms, faster than 94.78% of Python online submissions for Intersection of Two Linked Lists.
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        if headA is None or headB is None:
            return None
        
        curA = headA
        curB = headB
        while curA.next != None and curB.next != None:
            curA = curA.next
            curB = curB.next
        
        steps_left_to_None = 0
        if curA.next is None:
            long_list = headB
            short_list = headA
            while curB.next is not None:
                curB = curB.next
                steps_left_to_None += 1
        else: 
            long_list = headA
            short_list = headB
            while curA.next is not None:
                curA = curA.next
                steps_left_to_None += 1

        if curA != curB:
            return None
        
        for _ in range(steps_left_to_None):
            long_list = long_list.next
        
        while long_list != short_list:
            long_list = long_list.next
            short_list = short_list.next
        return long_list
            

    # Less codding solution
    # Tricky idea is
    def _getIntersectionNode(self, headA, headB):
        if not headA or not headB: return None
        p1 = headA
        p2 = headB

        while p1 != p2 and (p1 or p2):
            if not p1: p1 = headB
            if not p2: p2 = headA
            if p1 == p2: break
            p1 = p1.next
            p2 = p2.next

        return p1 if p1 == p2 else None