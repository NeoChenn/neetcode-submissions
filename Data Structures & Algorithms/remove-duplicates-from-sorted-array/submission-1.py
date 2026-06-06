class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        #Two pointers or a set
        mySet = set()
        k = 0
        i = 0
        while i < len(nums):
            if nums[i] in mySet:
                nums.remove(nums[i])
            else:
                mySet.add(nums[i])
                i += 1
                k += 1
        return k