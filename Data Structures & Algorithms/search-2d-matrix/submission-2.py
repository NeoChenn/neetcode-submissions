class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        #logm * logn
        #binary search on rows first

        l, r = 0, len(matrix) - 1
        lf, rt = 0, len(matrix[0]) - 1
        while l <= r:
            mid = l + (r - l) // 2
            if target < matrix[mid][0]:
                r = mid - 1
            elif target > matrix[mid][-1]:
                l = mid + 1
            else:
                while lf <= rt:
                    midCol = lf + (rt - lf) // 2
                    if target < matrix[mid][midCol]:
                        rt = midCol - 1
                    elif target > matrix[mid][midCol]:
                        lf = midCol + 1
                    else:
                        return True
                return False
        return False