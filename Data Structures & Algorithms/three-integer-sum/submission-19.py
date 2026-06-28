class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort() #[-4, -1, -1, 0, 1, 2]
        res = []
        for i in range(0, len(nums) - 2):
            if i != 0 and nums[i] == nums[i - 1]:
                continue
            j, k = i + 1, len(nums) - 1
            while j < k:
                if nums[i] + nums[j] + nums[k] == 0:
                    res.append([nums[i], nums[j], nums[k]])
                    dupej, dupek = nums[j], nums[k]
                    while j < k and nums[j] == dupej:
                        j += 1
                    while j < k and nums[k] == dupek:
                        k -= 1
                elif nums[i] + nums[j] + nums[k] < 0:
                    j += 1
                else:
                    k -= 1

        return res