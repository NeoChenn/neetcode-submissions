class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.maxHeap = []
        for n in nums:
            heapq.heappush(self.maxHeap, -n)

    def add(self, val: int) -> int:
        heapq.heappush(self.maxHeap, -val)
        popped = []
        for i in range(self.k):
            popped.append(heapq.heappop(self.maxHeap))
        kth = -popped[-1]
        for n in popped:
            heapq.heappush(self.maxHeap, n)
        return kth
        
