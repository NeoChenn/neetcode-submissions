class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        #binary search on weight capacity. from j to sum of all weights
        i, j = max(weights), sum(weights)
        minCapacity = j
        while i <= j:
            mid = (i + j) // 2
            #using that mid as the capacity, return how many days we need.
            d = 1
            weightOnShip = 0
            for weight in weights:
                if weight + weightOnShip > mid:
                    d += 1
                    weightOnShip = weight
                else:
                    weightOnShip += weight
            
            if d <= days:
                minCapacity = min(minCapacity, mid)
                j = mid - 1
            else:
                i = mid + 1
        return minCapacity