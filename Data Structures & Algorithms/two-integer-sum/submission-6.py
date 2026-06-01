class Solution: 
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = {}
        i = 0   
        while (True):
            value = target - nums[i]
            if (value in map.keys()):
                return [map[value], i]
            else:
                map[nums[i]] = i
                i += 1

            