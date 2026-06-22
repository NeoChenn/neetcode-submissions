class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        #base case: index >= len(nums)
        #choices: include/exclude
        #constraints: 

        res = []
        subset = []
        nums.sort()

        def bt_dfs(i):
            if i == len(nums):
                res.append(subset.copy())
                return

            subset.append(nums[i])
            bt_dfs(i + 1)
            subset.pop()

            while i + 1 < len(nums) and nums[i] == nums[i + 1]:
                i += 1
        
            bt_dfs(i + 1)

        bt_dfs(0)
        return res