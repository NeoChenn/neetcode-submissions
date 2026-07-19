class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []
        attempt = []
        seenAttempt = set()
        seenIndex = set()

        def backtrack():
            if len(attempt) == len(nums):
                if tuple(attempt) not in seenAttempt:
                    res.append(attempt.copy())
                    seenAttempt.add(tuple(attempt))
                return

            for i in range(len(nums)):
                if i not in seenIndex:
                    attempt.append(nums[i])
                    seenIndex.add(i)
                    backtrack()
                    attempt.pop()
                    seenIndex.remove(i)

        backtrack()
        return res