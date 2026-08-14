class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        """
        if equal, increase r by one and l = r - 1
        if sign doesn't flip, l = r - 1
        """
        longest = 2
        if (len(arr) == 1) or (len(arr) == 2 and arr[0] == arr[1]):
            return 1
        l, r = 0, 1
        while r < len(arr) and arr[r] == arr[r - 1]:
            l = r
            r += 1
        if r == len(arr):
            return 1
        isSmaller = arr[l] < arr[r]
        while r < len(arr):
            if arr[r - 1] == arr[r]:
                l = r
            elif arr[r - 1] < arr[r] and isSmaller:
                l = r - 1
            elif arr[r - 1] > arr[r] and not isSmaller:
                l = r - 1
            else:
                isSmaller = not isSmaller
                longest = max(longest, r - l + 1)
            r += 1
        
        return longest

        
