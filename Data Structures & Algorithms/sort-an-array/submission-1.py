class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:

        def sort(a, lo, hi):
            if (hi <= lo):
                return
        
            mid = lo + (hi - lo) // 2

            sort(a, lo, mid)
            sort(a, mid+1, hi)
            merge(a, lo, mid, hi)

        def merge(a, lo, mid, hi):
            left, right = a[lo:mid+1], a[mid+1: hi+1]
            i, l, r = lo, 0, 0

            while l < len(left) and r < len(right):
                if left[l] <= right[r]:
                    a[i] = left[l]
                    l += 1
                    i += 1
                else:
                    a[i] = right[r]
                    r += 1
                    i += 1
                
            while l < len(left):
                a[i] = left[l]
                l += 1
                i += 1

            while r < len(right):
                a[i] = right[r]
                i += 1
                r += 1

        sort(nums, 0, len(nums)-1)

        return nums

#merge sort
#merge step. Divide by half. In a new array, compare sorted left anf right sides
