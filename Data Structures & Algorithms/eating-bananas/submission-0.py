import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        res = r
        while l <= r:
            mid = (l + r) // 2
            hrs = sum(math.ceil(p / mid) for p in piles)
            if hrs <= h:
                res = mid       # mid works, but try smaller
                r = mid - 1
            else:
                l = mid + 1     # mid too slow, need bigger k
        return res