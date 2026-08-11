class Node:

    def __init__(self, key = None, val = None, nxt = None, prev = None):
        self.val = val
        self.key = key
        self.nxt = nxt
        self.prev = prev

class LRUCache:

    def __init__(self, capacity: int):
        """
        hashmap that maps keys to doubly linked list nodes
        initialise DLL with left dummy node (LRU) and right dummy node (MRU)
        on get, find node with hashmap[key] and get return node.value
        on put, update value if key exists in hashmap
            otherwise, if over capacity, remove LRU from hashmap and DLL
            add pair to hashmap and to right side of DLL
        """
        
        self.capacity = capacity
        self.keyToNode = {}
        self.lruDummy = Node()
        self.mruDummy = Node()
        self.lruDummy.nxt, self.mruDummy.prev = self.mruDummy, self.lruDummy 

    def removeFromDLL(self, key):
        node = self.keyToNode[key]
        node.prev.nxt = node.nxt
        node.nxt.prev = node.prev
    
    def addToDLL(self, node):
        node.nxt = self.mruDummy
        node.prev = self.mruDummy.prev
        self.mruDummy.prev.nxt = node
        self.mruDummy.prev = node

    def get(self, key: int) -> int:
        if key not in self.keyToNode:
            return -1
        #update DLL by removing from DLL and adding it to the left of DLL
        self.removeFromDLL(key) 
        self.addToDLL(self.keyToNode[key])
        return self.keyToNode[key].val

    def put(self, key: int, value: int) -> None:
        if key in self.keyToNode:
            self.keyToNode[key].val = value
            self.removeFromDLL(key)
            self.addToDLL(self.keyToNode[key])
            return
        if self.capacity == len(self.keyToNode):
            # delete LRU from DLL and from hashmap
            lruNode = self.lruDummy.nxt
            self.removeFromDLL(lruNode.key)
            self.keyToNode.pop(lruNode.key)


        newNode = Node(key, value)
        self.keyToNode[key] = newNode
        #add newNode to DLL
        self.addToDLL(newNode)

        
