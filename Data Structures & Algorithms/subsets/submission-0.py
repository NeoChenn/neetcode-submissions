class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        subset = []

        def bt_dfs(i):
            if i == len(nums):
                res.append(subset.copy())
                return
            
            #choice is to either append nums[i] or not append nums[i]
            subset.append(nums[i])
            bt_dfs(i + 1)
            subset.pop()

            bt_dfs(i + 1)

        bt_dfs(0)
        return res
            

#                  e
#             /  /  \  \ 
#            1  2   3   e