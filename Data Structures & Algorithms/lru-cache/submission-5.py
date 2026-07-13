class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        #hashmap to store key-value pairs
        #minheap to determine least used key. 
        #sort based on a time variable that increases for each get/put operation

        self.pairs = {} #key : [value, time]
        self.heap = []
        self.time = 0

    def get(self, key: int) -> int:
        #returns value if exists, otherwise returns -1
        if key not in self.pairs:
            return -1
        self.time += 1
        self.pairs[key][1] = self.time
        self.heap = [(v[1], k) for k, v in self.pairs.items()]
        heapq.heapify(self.heap)  
        return self.pairs[key][0]

    def put(self, key: int, value: int) -> None:
        #update value if key exists
        #if not, add key-value pair to cache
        #if introducing new pair causes cache to exceed its capacity, remove the least recently used key
        self.time += 1
        if key in self.pairs:
            self.pairs[key][0] = value
            self.pairs[key][1] = self.time
            self.heap = [(v[1], k) for k, v in self.pairs.items()]
            heapq.heapify(self.heap)  
        elif key not in self.pairs and len(self.pairs) + 1 <= self.capacity:
            self.pairs[key] = [value, self.time]
            heapq.heappush(self.heap, (self.time, key))
        else:
            lru = heapq.heappop(self.heap)
            self.pairs.pop(lru[1])
            self.pairs[key] = [value, self.time]
            heapq.heappush(self.heap, (self.time, key))