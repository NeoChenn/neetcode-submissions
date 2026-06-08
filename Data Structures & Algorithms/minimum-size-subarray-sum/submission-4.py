class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        sum = 0
        l, r = 0, 0

        while sum < target:
            if not r < len(nums):
                return 0
            sum += nums[r]
            r += 1
        r -= 1
        length = r - l + 1

        while r < len(nums):
            while sum >= target:
                length = min(length, r - l + 1)
                sum -= nums[l]
                l += 1
            r += 1
            if not r < len(nums):
                break
            sum += nums[r]

        return length
        #Sliding window. Pointer l and r at index 0
        #Increment r (updating sum) until sum >= target.
        #length = min(length, r - l + 1) 
        #while sum >= target, sum -= nums[l] and increment l and update length

