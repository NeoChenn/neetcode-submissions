class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        #[1, 3, 5, 7, 9, 11, 13] #12
        #find largest value smaller or equal to x. Two pointer with that and the next value
        #edge cases. If x <= arr[0] or x >= arr[-1]

        if x <= arr[0]:
            return arr[:k]
        if x >= arr[-1]:
            return arr[-k:]

        l, r = 0, len(arr) - 1
        z = 0
        while l <= r:
            mid = (l + r) // 2
            if arr[mid] > x:
                r = mid - 1
            elif arr[mid] <= x:
                z = max(z, mid)
                l = mid + 1

        l, r = z, z + 1
        while r - l - 1 != k:
            if r >= len(arr):
                l -= 1
            elif l < 0:
                r += 1
            elif abs(arr[l] - x) <= abs(arr[r] - x):
                l -= 1
            else:
                r += 1

        return arr[l + 1:r]