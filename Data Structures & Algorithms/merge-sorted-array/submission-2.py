class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i, j = 0, 0
        while i < m and j < n:
            if nums2[j] <= nums1[i]:
                nums1.pop()
                nums1.insert(i, nums2[j])
                m += 1
                i += 1
                j += 1
                continue
            i += 1
        while j < n:
            nums1[i] = nums2[j]
            i += 1
            j +=1