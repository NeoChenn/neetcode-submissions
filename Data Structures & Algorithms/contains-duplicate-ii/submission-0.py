class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        mySet = set()
        l = 0
        for r in range(len(nums)):
            if r - l > k:
                mySet.remove(nums[l])
                l += 1
            if nums[r] not in mySet:
                mySet.add(nums[r])
            else:
                return True
        return False