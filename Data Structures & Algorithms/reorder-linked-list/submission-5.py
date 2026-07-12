# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, node, dummy):
        if not node or not node.next:
            dummy.next = node
            return node

        self.reverseList(node.next, dummy).next = node
        node.next = None
        return node

    def reorderList(self, head: Optional[ListNode]) -> None:
        #find midpoint
        slow, fast = head, head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        #reverse list
        dummy = ListNode()
        second_half = slow.next
        slow.next = None
        self.reverseList(second_half, dummy)

        #modify list
        first, second = head, dummy.next
        while second:
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1
            first = tmp1
            second = tmp2



        