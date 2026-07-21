class Solution:
    def integerBreak(self, n: int) -> int:
        #recursive function returns maximum product at specific sum
        choices = [i for i in range(1, n + 1)]
        memo = {}

        def dfs(summ):
            if summ in memo:
                return memo[summ]
            if summ == n:
                return 1
            best = 0
            for choice in range(1, n - summ + 1):
                best = max(best, choice * dfs(summ + choice))
            memo[summ] = best
            return best
        
        best = 0
        for choice in range(1, n):
            best = max(best, choice * dfs(choice))
        return best