# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode()
        node = dummy
        index = 1
        # head = [1, 2, 3, 4, 5, 6, 7], left = 3, right = 6
        # append as normal until reaching left - 1, without a next for now

        # 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7
        #           3 <- 4 <- 5 <- 6
        # 1 -> 2 -> 6 -> 5 -> 4 -> 3 -> 7

        #value at position left - 1 points to value at position right
        #value at position left points to value at position right + 1
        #reverse as normal, keeping a pointer at left and right 

        curr = head
        while index < left:
            node.next = curr
            curr = curr.next
            node = node.next
            index += 1
        nodeLeftMinusOne = node
        nodeLeft = curr

        inverseDummy = ListNode()
        prev, curr = inverseDummy, curr
        while index < right:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
            index += 1
        nodeLeftMinusOne.next = curr
        nxt = curr.next
        curr.next = prev
        prev = curr
        curr = nxt
        nodeLeft.next = curr
        return dummy.next