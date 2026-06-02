class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        map = {}
        freq = len(nums) // 2

        for num in nums:
            if num in map:
                map[num] += 1
                if map[num] > freq:
                    return num
            else:
                map[num] = 1
        return num

#hashmap with num as key, frequency as value
#whenever frequency >= n / 2, return num

