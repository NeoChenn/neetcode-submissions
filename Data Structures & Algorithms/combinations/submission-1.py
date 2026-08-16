class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        #base case: add to res if len(attempt) == k, ignore if val reaches n and len != k 
        
        res = []
        attempt = []

        def bt(num):
            if len(attempt) == k:
                res.append(attempt.copy())
                return
            if num > n:
                return

            attempt.append(num)
            bt(num + 1)
            attempt.pop()

            bt(num + 1)

        bt(1)
        return res