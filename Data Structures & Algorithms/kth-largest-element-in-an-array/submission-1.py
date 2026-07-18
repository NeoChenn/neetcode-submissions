class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heapq.heapify_max(nums)
        kth = nums[0]
        for i in range(k):
            kth = heapq.heappop_max(nums)

        return kth
