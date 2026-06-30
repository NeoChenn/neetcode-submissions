class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = [[]]
        curr = []
        def backtrack(i):
            if i == len(nums):
                return

            curr.append(nums[i])
            res.append(curr.copy())
            backtrack(i + 1)
            curr.pop()

            backtrack(i + 1)

        backtrack(0)
        return res
            
            