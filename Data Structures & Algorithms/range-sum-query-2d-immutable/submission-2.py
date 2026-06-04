class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.matrix = matrix

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        sum = 0
        for x in range (row1, row2 + 1): #(2, 4)
            for y in range (col1, col2 + 1): #(1, 3)
                sum += self.matrix[x][y]
        return sum


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)

#Nested for loop
#for row 1 until row 2
    #for col 1 until col 2
