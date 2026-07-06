class Solution:
    def rob(self, nums: List[int]) -> int:
        memo = {}

        def recursion(i):
            if i >= len(nums):
                return 0

            if i in memo:
                return memo[i]
            
            memo[i] = max(recursion(i + 1), nums[i] + recursion(i + 2))
            return memo[i]

        return recursion(0)