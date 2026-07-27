class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        
        memo = {}

        def backtrack(total):
            if total in memo:
                return memo[total]
            if total == target:
                return 1
            if total > target:
                return 0

            ways = 0
            for n in nums:
                ways += backtrack(total + n)

            memo[total] = ways
            return ways
        
        return backtrack(0)