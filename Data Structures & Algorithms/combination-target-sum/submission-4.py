class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        #base case: sum > 9, return. sum == 9, append to res and return
        #choices: include/exclude
        
        res = []
        attempt = []

        def backtrack(i, total):
            if total == target:
                res.append(attempt.copy())
                return
            if total > target or i == len(nums):
                return
                
            attempt.append(nums[i])
            backtrack(i, total + nums[i])
            attempt.pop()

            backtrack(i + 1, total)

        backtrack(0, 0)
        return res
            