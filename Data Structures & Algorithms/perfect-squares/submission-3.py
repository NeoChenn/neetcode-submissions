class Solution:
    def numSquares(self, n: int) -> int:
        sys.setrecursionlimit(20000)
        """
        perfect square candidates range are between 1 and n 
        [i**2 for i in range(len(math.floor(math.sqrt(n)) + 1))]

        find all possible number of perfect squares that sum to n, return the smallest one

        my function returns the least number of perfect square numbers that sum to n
        """

        candidates = [i**2 for i in range(1, math.floor(math.sqrt(n)) + 1)]
        cache = {n : 0}

        def recursion(total):
            if total in cache:
                return cache[total]

            minimum = n
            for candidate in candidates:
                if total + candidate <= n:
                    minimum = min(minimum, recursion(total + candidate))
            
            cache[total] = 1 + minimum
            return cache[total]
        
        return recursion(0)