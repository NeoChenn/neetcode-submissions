class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #place into hashmap. key is num, value is index
        #for each num, see if (target - num) is in hashmap
        #if it is, return indices. Otherwise, continue

        myMap = {}
        for i, n in enumerate(nums):
            if n in myMap:
                return [myMap[n], i]
            myMap[target - n] = i

