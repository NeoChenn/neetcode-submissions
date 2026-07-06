class Solution:
    def rob(self, nums: List[int]) -> int:
        memo = {}

        def recursion(i, length):
            if i >= length:
                return 0

            if i in memo:
                return memo[i]
            
            memo[i] = max(recursion(i + 1, length), nums[i] + recursion(i + 2, length))
            return memo[i]

        excludeFirst = recursion(0, len(nums) - 1)
        memo.clear()
        excludeLast = recursion(1, len(nums))
        return max(nums[0], excludeFirst, excludeLast)