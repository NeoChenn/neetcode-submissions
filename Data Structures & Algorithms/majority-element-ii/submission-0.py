class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        floor = len(nums) // 3
    
        arr = []
        map = {}
        for n in nums:
            if n not in map:
                map[n] = 1
            else:
                map[n] += 1
    
        for n in map:
            if map[n] > floor:
                arr.append(n)
        return arr