class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l, r = 0, len(matrix) * len(matrix[0]) - 1

        if target < matrix[0][0] or target > matrix[-1][-1]:
            return False

        #divide mid by len(matrix) gives row. mod mid by len(matrix) gives col.
        while l <= r:
            mid = (l + r) // 2
            if matrix[mid // len(matrix[0])][mid % len(matrix[0])] < target:
                l = mid + 1
            elif matrix[mid // len(matrix[0])][mid % len(matrix[0])] > target:
                r = mid - 1
            else:
                return True
        
        return False