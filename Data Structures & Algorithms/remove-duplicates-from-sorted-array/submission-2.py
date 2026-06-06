class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i, j = 0, 1
        #delete nums[j] until nums[j] != nums[i]
        #increment i and j and repeat previous step until j == len(nums)

        while j < len(nums):
            while j < len(nums) and nums[j] == nums[i]:
                nums.remove(nums[j])
            j += 1
            i += 1

        return len(nums)