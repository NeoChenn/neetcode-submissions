class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0
        j = len(nums) - 1
        k = 0
        while i <= j:
            if nums[i] != val:
                k = k + 1
                i = i + 1
                continue
            if nums[j] == val:
                j = j - 1
                continue
            # nums[i] == val and nums[j] != val
            temp = nums[i]
            nums[i] = nums[j]
            nums[j] = temp
        return k
            
#sort nums in-place, such that all the values != val are moved to the front
#Pointer at the start i = 0   
#Pointer at the end j = len(nums) - 1
#while i != j
#while nums[i] != val, i += 1 and k += 1. while nums[j] == val, j -= 1
#If nums[i] == val, swap nums[i] with nums[j].
#if i == j, return k

