class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        sumToTarget = []
        
        #base case: sum == target
        #choices: nums. Can repeat
        #restrictions: must sum to target. Discard if sum larger than target. 
        #backtrack step: pop

        def bt_dfs(i, acc):
            if acc == target:
                res.append(sumToTarget.copy())
                return
            elif acc > target:
                return

            for j in range(i, len(nums)):
                sumToTarget.append(nums[j])
                bt_dfs(j, acc + nums[j])
                sumToTarget.pop()

        bt_dfs(0, 0)
        return res
