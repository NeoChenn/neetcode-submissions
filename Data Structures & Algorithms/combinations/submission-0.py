class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        """
        base case: length == k or index > n
        """
        res = []
        attempt = []

        def backtrack(num):
            if len(attempt) == k:
                res.append(attempt.copy())
                return
            if num > n:
                return

            attempt.append(num)
            backtrack(num + 1)
            attempt.pop()
            
            backtrack(num + 1)

        backtrack(1)
        return res