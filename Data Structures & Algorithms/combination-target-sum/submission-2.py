class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        #base case: sum >= target
        #choices: can choose unlimited times, or skip each number. 
        #constraints: no two same combinations
        #backtrack step
        res = []
        attempt = []

        def dfs(total, ind):
            if total >= target:
                if total == target:
                    res.append(attempt.copy())
                return

            for i in range(ind, len(nums)):
                attempt.append(nums[i])
                dfs(total + nums[i], i)
                attempt.pop()

        dfs(0, 0)
        return res
