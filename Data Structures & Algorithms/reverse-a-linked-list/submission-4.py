# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()

        def recursion(node):
            if not node or not node.next:
                dummy.next = node
                return node

            recursion(node.next).next = node
            node.next = None
            return node

        recursion(head)
        return dummy.next