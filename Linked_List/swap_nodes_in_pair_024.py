# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# class Solution:
#     def swapPairs(self, head: 'ListNode') -> 'ListNode':
#         dummy_head = ListNode(0)
#         dummy_head.next = head
#         prev = dummy_head
        
#         while head and head.next:
#             tmp = head.next
#             head.next = tmp.next
#             tmp.next = head
#             prev.next = tmp
#             prev = head
#             head = head.next
            

            
#         return dummy_head.next

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x, next=None):
        self.val = x
        self.next = next

class Solution:
    def swapPairs(self, head: 'ListNode') -> 'ListNode':
        dummy_head = ListNode(0)
        dummy_head.next = head

        curr = dummy_head.next
        
        while curr and curr.next:
            temp = curr.next
            curr.next = temp.next
            temp.next = dummy_head.next
            dummy_head.next = temp

        while dummy_head.next:
            dummy_head = dummy_head.next
            print(dummy_head.val)
        # return dummy_head.next

LL = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
Solution().swapPairs(LL)