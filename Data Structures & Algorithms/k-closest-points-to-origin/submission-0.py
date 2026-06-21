class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        arr = []
        res = []
        #in a min heap, store (dist, [xi, yi])
        for p in points:
            heapq.heappush(arr, (math.sqrt(p[0]**2 + p[1]**2), p))

        def dist(a, b):
            return math.sqrt(a**2 + b**2)

        for i in range(k):
            res.append(heapq.heappop(arr)[1])

        return res