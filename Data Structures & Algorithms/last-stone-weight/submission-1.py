class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heapq.heapify_max(stones)
        while len(stones) >= 2:
            a = heapq.heappop_max(stones)
            b = heapq.heappop_max(stones)
            if a == b:
                continue
            heapq.heappush_max(stones, abs(a - b))

        if len(stones) == 1:
            return stones[0]
        else:
            return 0