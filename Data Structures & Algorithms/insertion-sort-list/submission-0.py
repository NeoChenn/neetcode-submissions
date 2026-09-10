# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        currUnsorted = head
        while currUnsorted:
            curr = dummy
            while True:
                if not curr.next:
                    curr.next = ListNode(currUnsorted.val)
                    currUnsorted = currUnsorted.next
                    break
                elif currUnsorted.val > curr.next.val:
                    curr = curr.next
                else:
                    tmp = curr.next
                    curr.next = ListNode(currUnsorted.val)
                    curr.next.next = tmp
                    currUnsorted = currUnsorted.next
                    break
        return dummy.next