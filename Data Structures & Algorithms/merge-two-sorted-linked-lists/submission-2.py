# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        #start pointer at head of each ll. 
        #append the smaller value to new ll and move respective pointer
        #repeat process until either pointer reaches the end. add remaining onto tail

        curr1 = list1
        curr2 = list2
        dummy = ListNode()
        curr = dummy

        while curr1 and curr2:
            if curr1.val < curr2.val:
                curr.next = ListNode(curr1.val)
                curr = curr.next
                curr1 = curr1.next
            else:
                curr.next = ListNode(curr2.val)
                curr = curr.next
                curr2 = curr2.next

        if curr1:
            curr.next = curr1

        if curr2:
            curr.next = curr2

        return dummy.next