class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 0 
        num = nums[0]

        for n in nums:
            if count == 0:
                num = n
            if n == num:
                count += 1
            else:
                count -= 1
        
        return num