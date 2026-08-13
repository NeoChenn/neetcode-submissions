class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []
        attempt = []
        nums.sort()
        visited = set()

        def bt():
            if len(attempt) == len(nums):
                res.append(attempt.copy())
                return
            
            repeats = set()
            for i in range(len(nums)):
                if i in visited:
                    continue
                if nums[i] in repeats:
                    continue
                repeats.add(nums[i])
                attempt.append(nums[i])
                visited.add(i)
                bt()
                attempt.pop()
                visited.remove(i)
        
        bt()
        return res