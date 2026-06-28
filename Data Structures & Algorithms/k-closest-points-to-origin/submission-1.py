class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        res = []
        for x, y in points:
            heap.append((math.sqrt(x**2 + y**2),x, y))
        
        heapq.heapify(heap)
        for i in range(k):
            item = heapq.heappop(heap)
            res.append([item[1], item[2]])

        return res