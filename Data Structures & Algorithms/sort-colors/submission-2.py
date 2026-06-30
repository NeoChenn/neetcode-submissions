class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        #hashmap that counts freq of each color
        #modify array inplace according to the freq of each color

        freq = {0: 0, 1: 0, 2: 0}
        for n in nums:
            freq[n] += 1

        j = 0
        for i in range(3):
            while freq[i] != 0:
                nums[j] = i
                j += 1
                freq[i] -= 1
