# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head: 'ListNode', n: 'int') -> 'ListNode':
        dummy_head = ListNode(0)
        dummy_head.next = head
        
        fast = dummy_head.next
        for _ in range(n):
            fast = fast.next
        
        slow = dummy_head
        while fast:
            fast = fast.next
            slow = slow.next
        
        # we are behind the node to be deleted
        slow.next = slow.next.next
            
        return dummy_head.next