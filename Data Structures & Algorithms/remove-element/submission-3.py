class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0
        j = len(nums) - 1
        k = 0
        while i <= j:
            if nums[i] != val:
                k += 1
                i += 1
            elif nums[j] == val:
                j -= 1
            else:
                # nums[i] == val and nums[j] != val
                nums[i], nums[j] = nums[j], nums[i]
                k += 1
                i += 1
                j -= 1
        return k