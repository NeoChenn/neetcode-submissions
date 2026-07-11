class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        #two pointers. 
        #One at intended position of unique element
        #Other in search of next unique element
        #Swap and repeat

        i, j = 1, 1
        while j < len(nums):
            while nums[j] == nums[i - 1]:
                if j == len(nums) - 1:
                    return i
                j += 1
            nums[i] = nums[j]
            i += 1
        return i
            
        #[0, 1, 2, 3, 1i, 2, 2, 3, 3, 3j]