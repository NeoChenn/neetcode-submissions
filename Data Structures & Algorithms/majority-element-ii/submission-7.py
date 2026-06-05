import math

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        floor = math.floor(len(nums) / 3)
        arr = []

        i = 0
        while i < len(nums):
            count = 1
            temp = nums[i]
            nums.remove(temp)
            while temp in nums:
                count += 1
                nums.remove(temp)
            if count > floor:
                arr.append(temp)
        
        return arr