class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {n+1 : 0, n : 1}

        def topDown(num):
            if num in memo:
                return memo[num]
            else:
                memo[num] = topDown(num + 1) + topDown(num + 2)
                return memo[num]

        return topDown(0)