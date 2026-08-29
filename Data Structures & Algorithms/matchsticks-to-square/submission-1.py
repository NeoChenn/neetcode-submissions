class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        """
        group matchsticks into groups of 4 with each groups' total length being equal
        calculate total and divide it by 4. That's what each group must sum up to
        if possible, return True
        otherwise, return False

        backtrack:
        for each matchstick, place it in one of 4 buckets and keep track of the sum for each bucket
        base case is when all matchsticks have been placed.
        constraints: all buckets must have at least 1 matchstick.
                     the sum of each bucket cannot be larger than a certain value
        """

        sideLengths = [0, 0, 0, 0]
        emptyBuckets = 4
        correctLength = sum(matchsticks) / 4
        if len(matchsticks) < 4 or matchsticks[-1] > correctLength or not correctLength.is_integer():
            return False
        
        def backtrack(i):
            nonlocal emptyBuckets
            nonlocal correctLength
            if i >= len(matchsticks):
                for l in sideLengths:
                    if l != correctLength:
                        return False
                return True


            for idx in range(len(sideLengths)):
                if sideLengths[idx] + matchsticks[i] <= correctLength:
                    if sideLengths[idx] == 0:
                        emptyBuckets -= 1
                    sideLengths[idx] += matchsticks[i]
                    if backtrack(i + 1):
                        return True
                    sideLengths[idx] -= matchsticks[i]
                    if sideLengths[idx] == 0:
                        emptyBuckets += 1
            return False

        return backtrack(0)
            