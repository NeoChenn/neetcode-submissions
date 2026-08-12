class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        attempt = []
        visited = set()

        def bt():
            if len(attempt) == len(nums):
                res.append(attempt.copy())
                return
            
            for i in range(len(nums)):
                if i in visited:
                    continue
                attempt.append(nums[i])
                visited.add(i)
                bt()
                attempt.pop()
                visited.remove(i)
        
        bt()
        return res