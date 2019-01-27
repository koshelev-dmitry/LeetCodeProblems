# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        result = newList = ListNode(None)
        while l1 and l2:
            if l1.val > l2.val:
                if newList.val is None:
                    newList.val = l2.val
                else:
                    newList.next = ListNode(l2.val)
                    newList = newList.next
                l2 = l2.next
            else:
                if newList.val is None:
                    newList.val = l1.val
                else:
                    newList.next = ListNode(l1.val)
                    newList = newList.next
                l1 = l1.next
        if not l1:
            l = l2
        else:
            l = l1
        while l:
            if newList.val is None:
                newList.val = l.val
            else:
                newList.next = ListNode(l.val)
                newList = newList.next
            l = l.next
        return result if result.val is not None else []

l1 = ListNode(1)
l1.next = ListNode(3)
l1.next.next = ListNode(4)

l2 = ListNode(1)
l2.next = ListNode(2)
l2.next.next = ListNode(4)

solution = Solution()
l3 = solution.mergeTwoLists(l1, l2)
while l3:
    print(l3.val)
    l3 = l3.next