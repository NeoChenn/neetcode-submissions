class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:

        memo = {len(cost) : 0, len(cost) + 1 : 0}

        def dfs(i):
            if i in memo:
                return memo[i]
            memo[i] = cost[i] + min(dfs(i + 1), dfs(i + 2))
            return memo[i]

        dfs(0) 
        dfs(1)
        return min(memo[0], memo[1])

