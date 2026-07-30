class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        """
            add [[a, 'a'], [b, 'b'], [c, 'c']] to a maxHeap
            pop. if does create x3 contig, pop again reduce index 0 by one, append index 1 to output
            if index 0 != 0, add back to maxHeap
        """

        res = []
        maxHeap = []
        if a != 0:
            maxHeap.append([a, 'a'])
        if b != 0:
            maxHeap.append([b, 'b'])
        if c != 0:
            maxHeap.append([c, 'c'])
        heapq.heapify_max(maxHeap)

        while maxHeap:
            cur = heapq.heappop_max(maxHeap)
            if len(res) >= 2 and res[-1] == cur[1] and res[-2] == cur[1] and not maxHeap:
                return "".join(res)
            elif len(res) >= 2 and res[-1] == cur[1] and res[-2] == cur[1] and maxHeap:
                cur2 = heapq.heappop_max(maxHeap)
                cur2[0] -= 1
                res.append(cur2[1])
                if cur2[0] != 0:
                    heapq.heappush_max(maxHeap, cur2)
                heapq.heappush_max(maxHeap, cur)
                continue
            else:
                cur[0] -= 1
                res.append(cur[1])
                if cur[0] != 0:
                    heapq.heappush_max(maxHeap, cur)
        return "".join(res)