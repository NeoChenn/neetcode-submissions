class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """  
            sort first: [-4, -1, -1, 0, 1, 2]
        """    
        nums.sort()
        res = []
        for i in range(len(nums) - 2):
            if i != 0 and nums[i] == nums[i - 1]:
                continue
            l, r = i + 1, len(nums) - 1
            while l < r:
                if nums[i] + nums[l] + nums[r] == 0:
                    res.append([nums[i], nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while l < len(nums) and nums[l] == nums[l - 1]:
                        l += 1
                    while r > i and nums[r] == nums[r + 1]:
                        r -= 1
                    if not l < r:
                        break
                elif nums[i] + nums[l] + nums[r] < 0:
                    l += 1
                else:
                    r -= 1
        return res
        