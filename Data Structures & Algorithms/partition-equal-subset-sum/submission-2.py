class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        memo = {}
        total = sum(nums)
        if total % 2 != 0:
            return False
        target = total // 2

        def dfs(i, remaining):
            if remaining == 0:
                return True
            if i >= len(nums) or remaining < 0:
                return False
            if (i, remaining) in memo:
                return memo[(i, remaining)]
            
            memo[(i, remaining)] = dfs(i + 1, remaining - nums[i]) or dfs(i + 1, remaining)
            return memo[(i, remaining)]

        return dfs(0, target)