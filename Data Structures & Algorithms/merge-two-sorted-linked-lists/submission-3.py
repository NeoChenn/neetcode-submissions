# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        curr = dummy

        cur1, cur2 = list1, list2

        while cur1 and cur2:
            if cur1.val <= cur2.val:
                tmp = cur1.next
                cur1.next = None
                curr.next = cur1
                cur1 = tmp
                curr = curr.next
            else:
                tmp = cur2.next
                cur2.next = None
                curr.next = cur2
                cur2 = tmp
                curr = curr.next
        
        if cur1:
            curr.next = cur1
        
        if cur2:
            curr.next = cur2

        return dummy.next