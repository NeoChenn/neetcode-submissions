class ListNode:
    
    def __init__(self, val = None, next = None):
        self.val = val
        self.next = next

class MyHashSet:

    def __init__(self):
        self.hashset = [ListNode() for _ in range(10000)] #dummy node at each index 

    def add(self, key: int) -> None:
        node = self.hashset[key % 10000]
        while node.next:
            if node.next.val == key:
                return
            node = node.next
        node.next = ListNode(key)

    def remove(self, key: int) -> None:
        node = self.hashset[key % 10000].next
        prev = self.hashset[key % 10000]
        while node:
            if node.val == key:
                prev.next = prev.next.next
                break
            prev = node
            node = node.next

    def contains(self, key: int) -> bool:
        node = self.hashset[key % 10000].next
        while node:
            if node.val == key:
                return True
            node = node.next
        return False


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)