class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        attempt = []
        visited = set()

        def recursion():
            if len(attempt) == len(nums):
                res.append(attempt.copy())
            
            for n in nums:
                if n in visited:
                    continue
                attempt.append(n)
                visited.add(n)
                recursion()
                attempt.pop()
                visited.remove(n)
        
        recursion()
        return res