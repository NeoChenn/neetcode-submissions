class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l = 0
        total = 0
        res = 999999

        for r in range(len(nums)):
            total += nums[r]
            if total < target:
                continue
            while total - nums[l] >= target:
                total -= nums[l]
                l += 1
            res = min(res, r - l + 1)
        
        if res == 999999:
            return 0
        return res

