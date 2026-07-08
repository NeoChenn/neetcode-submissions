class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        #base case: sum == target, add res list. sum > target, do nothing. return
        
        res = []
        attempt = []

        def backtrack(i, total):
            if i >= len(nums) or total >= target:
                if total == target:
                    res.append(attempt.copy())
                return

            attempt.append(nums[i])
            backtrack(i, total + nums[i])
            attempt.pop()
            backtrack(i + 1, total)
        
        backtrack(0, 0)
        return res