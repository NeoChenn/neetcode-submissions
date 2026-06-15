class Solution:
    def search(self, nums: List[int], target: int) -> int:
        #Find the index that separates both halves        
        indexOfSmallest = len(nums) - 1
        l, r = 0, len(nums) - 1

        while l <= r:
            if nums[l] < nums[r]:
                indexOfSmallest = l
                break

            mid = (l + r) // 2
            if nums[mid] < nums[indexOfSmallest]:
                indexOfSmallest = mid
            
            if nums[mid] >= nums[l]:
                l = mid + 1
            else:
                r = mid - 1
            
        #Find in which half the target could be in
        l, r = 0, len(nums) - 1
        if target >= nums[indexOfSmallest] and target <= nums[r]:
            l = indexOfSmallest
        else:
            r = indexOfSmallest - 1
        
        #check if target in this half
        while l <= r:
            mid = (l + r) // 2
            if target > nums[mid]:
                l = mid + 1
            elif target < nums[mid]:
                r = mid - 1
            else:
                return mid
        return -1
        
        #[3, 4, 5, 6, 1, 2]
        #1. find in which half the target is. then 2. check if target in that half
        #find the min value, which separates both halves.
        #if mid >= l, l = mid + 1
        #elif mid < l, r = mid - 1, update smallest val
        #if l < r, break.
        #every element in second half is smaller than first half

