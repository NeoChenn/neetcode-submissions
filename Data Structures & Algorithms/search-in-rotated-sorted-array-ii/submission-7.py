class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        """
        observations:
        split into two sorted parts
        all nums in the right will be smaller that the ones in the left
        the smallest num of the left side is nums[0]
        the largest num of the right side is nums[-1]

        to check which side nums[mid] is in, compare with nums[0]
            if nums[mid] > nums[0], we're on the left side
            if nums[mid] < nums[0], we're on the right side
        if nums[mid] > target, 
            if on left side (e.g. [3, 4, 4, 5, 6, 1, 2, 2], target = 1)
                if target > nums[0], target within left side, r = mid - 1
                elif target < nums[0], target within right side, l = mid + 1
            if on right side (e.g. [5, 6, 1, 2, 3, 4, 4], target = 1)
                r = mid - 1
        if nums[mid] < target,
            if on left side (e.g. [3, 4, 5, 6, 1, 2], target = 10)
                l = mid + 1
            if on right side (e.g. [5, 6, 1, 2, 3, 4])
                if target > nums[0], target within left side, r = mid - 1
                elif target < nums[0], target within right side, l = mid + 1
        else
            return True
        """
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                return True
            if nums[mid] > nums[l]:
                left = True
            elif nums[mid] < nums[l]:
                left = False
            else:
                l += 1
                continue

            if (nums[mid] > target and left) or (nums[mid] < target and not left):
                if target > nums[l]:
                    r = mid - 1
                elif target < nums[l]:
                    l = mid + 1
                else:
                    return True
            elif nums[mid] > target and not left:
                r = mid - 1
            elif nums[mid] < target and left:
                l = mid + 1
            else:
                return True
        return False