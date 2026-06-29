class Solution:
    def search(self, nums: List[int], target: int) -> int:
        #if nums[mid] > nums[0], we're on the left side
        #if nums[mid] < nums[0], we're on the right side

        #if on left side and target < nums[mid], if target < nums[0], target on right side.
        #if on left side and target > nums[mid], target toward right so move mid to right
        #if on right side and target < nums[mid], target toward left so move mid to left
        #if on right side and target > nums[mid], if target < nums[0], target on right side

        #[4, 5, 6, 7, 1, 2, 3]

        i, j = 0, len(nums) - 1
        while i <= j:
            mid = (i + j) // 2
            if target == nums[mid]:
                return mid
            if nums[mid] >= nums[0]: #left side
                if target > nums[mid]:
                    i = mid + 1
                else:
                    if target < nums[0]:
                        i = mid + 1 
                    else:
                        j = mid - 1
            
            else:   #right side
                if target < nums[mid]:
                    j = mid - 1
                else:
                    if target < nums[0]:
                        i = mid + 1
                    else:
                        j = mid - 1

        return -1
        