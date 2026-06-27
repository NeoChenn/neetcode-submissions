# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        curr = dummy

        if not head:
            return None

        def rev(node):
            if not node:
                return curr

            rev(node.next).next = node
            return node
        
        rev(head)
        head.next = None
        return dummy.next
            
