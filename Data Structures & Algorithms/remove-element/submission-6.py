class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i, j = 0, len(nums) - 1
        while i <= j:
            while i <= j and nums[i] != val:
                i += 1
            while i <= j and nums[j] == val:
                j -= 1
            if i <= j:
                nums[i], nums[j] = nums[j], nums[i]

        return i

        #[3i, 2, 2j, 3], [2, 2j, 3i, 3]
        #[0, 1, 2i, 2, 3, 0, 4j, 2], [0, 1, 4, 2i, 3, 0, 2, 2]