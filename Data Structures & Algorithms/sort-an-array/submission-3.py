import random

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        random.shuffle(nums)
        self.sort(nums, 0, len(nums)-1)
        return nums

    def sort(self, nums, lo, hi):
        if hi <= lo:
            return

        pivot = self.partitionStep(nums, lo, hi)
        self.sort(nums, lo, pivot-1)
        self.sort(nums, pivot+1, hi )

    def partitionStep(self, nums, lo, hi):
        pivot = nums[lo]
        i = lo + 1
        j = hi
        while True:
            while i <= hi and nums[i] <= pivot:
                i += 1
            while j > lo and nums[j] > pivot:
                j -= 1
            if i > j:
                nums[lo] = nums[j]
                nums[j] = pivot
                return j
            else:
                temp = nums[i]
                nums[i] = nums[j]
                nums[j] = temp
                continue

#quick sort:
#shuffle array
#i++ until nums[i] > nums[0]. j++ until nums[j] < nums[0] 
#swap(nums[i], nums[j])

