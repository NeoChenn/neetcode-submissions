class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        #Three pointers. i = 0, j = 0 and k = len(nums) - 1
        #i represents the end boundary of the 0s
        #k represents the start boundary of the 2s
        #j runs across the whole list
        #if nums[j] = 0, swap(nums[j], nums[i]) and increment i and j
        #if nums[j] = 2, swap (nums[j], nums[k]) and decrement k
        #if nums[j] = 1, increment j
        #repeat this until j = k

        i, j, k = 0, 0, len(nums) - 1
        while j <= k:
            if nums[j] == 0:
                nums[j], nums[i] = nums[i], nums[j]
                i += 1
                j += 1
            elif nums[j] == 1:
                j += 1
            else:
                nums[j], nums[k] = nums[k], nums[j]
                k -= 1