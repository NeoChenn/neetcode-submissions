class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        subset = []

        def subsetSum():
            result = 0
            for x in subset:
                result ^= x
            return result

        def bt(i):
            if i == len(nums):
                return subsetSum()
            
            total = 0
            subset.append(nums[i])
            total += bt(i + 1)
            subset.pop()
            total += bt(i + 1)
            return total
        
        return bt(0)