class Solution:
    def climbStairs(self, n: int) -> int:
        
        memo = {}

        def recursion(total):
            if total in memo:
                return memo[total]
            if total == n:
                return 1
            if total > n:
                return 0
            
            memo[total] = recursion(total + 1) + recursion(total + 2) 
            return memo[total]

        return recursion(0)