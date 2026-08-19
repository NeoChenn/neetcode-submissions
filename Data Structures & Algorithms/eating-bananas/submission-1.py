class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        """
        k can be between 1 and max(piles)
        binary search to try the k's
        if WORKS, reduce r pointer and update minimum k
        if DOESN'T WORK, increase l pointer

        to check if it works, for each pile, add math.ceil(piles[i] / mid) to time
        if time > h, doesn't work. if time <= h, works
        """

        l, r = 1, max(piles)
        minK = max(piles)
        while l <= r:
            mid = (l + r) // 2
            time = 0
            for pile in piles:
                time += math.ceil(pile / mid)
            if time <= h:
                r = mid - 1
                minK = min(minK, mid)
            else:
                l = mid + 1
        return minK