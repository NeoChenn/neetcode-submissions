class Solution:
    def mySqrt(self, x: int) -> int:
        l, r = 0, x
        mid = 0
        while l <= r:
            mid = (l + r) // 2
            if mid*mid == x:
                return mid
            elif mid*mid > x:
                r = mid - 1
            else:
                l = mid + 1

        if (mid + 1)*(mid + 1) < x:
            return mid + 1
        elif mid * mid < x:
            return mid
        else:
            return mid - 1
        #[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]