class Solution:
    def rob(self, nums: List[int]) -> int:
        memo = {}

        def recursion(i):
            if i >= len(nums):
                return 0

            if i in memo:
                return memo[i]

            memo[i] = max(nums[i] + recursion(i + 2), nums[i] + recursion(i + 3))
            return memo[i]
        
        return max(recursion(0), recursion(1))