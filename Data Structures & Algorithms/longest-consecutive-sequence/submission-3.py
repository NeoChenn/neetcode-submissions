class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums.sort()
        arr = [1]
        count = 1
        if nums == []:
            return 0
        for i in range(1, len(nums)):
            if nums[i-1] + 1 == nums[i]:
                count += 1
            elif nums[i-1] == nums[i]:
                continue
            else:
                arr.append(count)
                count = 1
        arr.append(count)
        
        arr.sort(reverse = True)
        return arr[0]


