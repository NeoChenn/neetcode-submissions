class Solution:
    def tribonacci(self, n: int) -> int:
        memo = {0 : 0, 1 : 1, 2 : 1} 

        def topBottom(num):
            if num in memo:
                return memo[num]
            memo[num] = topBottom(num - 1) + topBottom(num - 2) + topBottom(num - 3) 
            return memo[num]

        return topBottom(n)