class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        attempt = []
        def recursion(i):
            nonlocal res, attempt
            if i > len(nums) - 1:
                res.append(attempt.copy())
                return
            attempt.append(nums[i])
            recursion(i + 1)
            attempt.pop()
            recursion(i + 1)
        recursion(0)
        return res
