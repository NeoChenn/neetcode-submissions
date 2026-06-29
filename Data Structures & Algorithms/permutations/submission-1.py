class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        #base case: len(attempt) == len(nums)
        #choices: num in nums
        #constraints: no repeats
        res = []
        attempt = []
        attemptSet = set() #for O(1) lookups

        def backtrack():
            if len(attempt) == len(nums):
                res.append(attempt.copy())
                return
            
            for num in nums:
                if num not in attemptSet:
                    attempt.append(num)
                    attemptSet.add(num)
                    backtrack()
                    attempt.pop()
                    attemptSet.remove(num)
            
        backtrack()
        return res
