class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        """
        function returns the fewest number of coins needed to make up amount
        total change as parameter 
        """
        memo = {}

        def recursion(total):
            if total == amount:
                return 0
            if total > amount:
                return float('inf')
            if total in memo:
                return 1 + memo[total]
            minimum = float('inf')
            for coin in coins:
                minimum = min(minimum, recursion(total + coin))
            memo[total] = minimum
            return 1 + minimum  
        
        minimum = recursion(0)
        if minimum > 999999:
            return -1
        else:
            return minimum