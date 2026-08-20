class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        """
        either find target, or find the index of the smallest number bigger than target
        """
        res = len(nums)
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                l = mid + 1
            else:
                res = min(res, mid)
                r = mid - 1
    
        return res