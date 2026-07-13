class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        minimum = 100000
        l = 0
        curSum = 0
        for r in range(len(nums)):
            curSum += nums[r]
            while curSum >= target:
                minimum = min(minimum, r - l + 1)
                curSum -= nums[l]
                l += 1

        if minimum == 100000:
            return 0
        return minimum

