class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        sumToTarget = []
        
        #base case: sum == target
        #choices: nums. Can repeat
        #restrictions: must sum to target. Discard if sum larger than target
        #backtrack step: pop

        def bt_dfs(i):
            if sum(sumToTarget) == target:
                res.append(sumToTarget.copy())
                return
            elif sum(sumToTarget) > target:
                return

            for i in range(i, len(nums)):
                sumToTarget.append(nums[i])
                bt_dfs(i)
                sumToTarget.pop()

        bt_dfs(0)
        return res
