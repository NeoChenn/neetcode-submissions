class Solution:
    def canPartition(self, nums: List[int]) -> bool:

        memo = {}
        
        def dfs(i, sumDiff):
            if (i, sumDiff) in memo:
                return memo[(i, sumDiff)]
            if i == len(nums):
                if sumDiff == 0:
                    return True
                return False

            memo[(i, sumDiff)] = dfs(i + 1, sumDiff + nums[i]) or dfs(i + 1, sumDiff - nums[i])
            return memo[(i, sumDiff)]

        return dfs(0, 0)