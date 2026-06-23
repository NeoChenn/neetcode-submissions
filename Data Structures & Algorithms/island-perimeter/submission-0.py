class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        #perimeter varies with number of neighbours. 0, 1, 2, 3, 4 = 4, 3, 2, 1, 0
        maxRowIndex = len(grid)
        maxColIndex = len(grid[0])

        visited = set()
        self.perimeter = 0

        def dfs(row, col):
            if grid[row][col] == 0:
                return
            
            self.perimeter += 4
    
            neighbours = []
            if row + 1 < maxRowIndex: 
                neighbours.append((row + 1, col))
            if row - 1 >= 0:
                neighbours.append((row - 1, col))
            if col + 1 < maxColIndex:
                neighbours.append((row, col + 1))
            if col - 1 >= 0:
                neighbours.append((row, col - 1))

            for neighbour in neighbours:
                if grid[neighbour[0]][neighbour[1]] == 1:
                    self.perimeter -= 1
                if neighbour in visited:
                    continue
                visited.add((neighbour[0], neighbour[1]))
                dfs(neighbour[0], neighbour[1])

        for row in range(maxRowIndex):
            for col in range(maxColIndex):
                if grid[row][col] == 1:
                    visited.add((row, col))
                    dfs(row, col)
                    return self.perimeter