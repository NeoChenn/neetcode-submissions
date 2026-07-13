class LRUCache: #Same as solution3 but with "eviction"

    def __init__(self, capacity: int):
        self.capacity = capacity

        self.pairs = {} #key : [value, time]
        self.heap = []
        self.time = 0

    def get(self, key):
        if key not in self.pairs:
            return -1
        self.time += 1
        self.pairs[key][1] = self.time
        heapq.heappush(self.heap, (self.time, key))  # push new entry, old one becomes stale
        return self.pairs[key][0]

    def put(self, key, value):
        self.time += 1
        self.pairs[key] = [value, self.time]
        heapq.heappush(self.heap, (self.time, key))
        
        while len(self.pairs) > self.capacity:
            time, k = heapq.heappop(self.heap)
            if self.pairs.get(k, [None, None])[1] == time:  # not stale
                del self.pairs[k]