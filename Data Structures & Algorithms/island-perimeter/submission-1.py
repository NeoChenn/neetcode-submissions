class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        #Iterate through the grid to find one land block
        #run dfs on the land block and traverse through all land blocks
        #if neighbor of land block is out of bounds/water, increment perimeter by 1 for each side
        
        perimeter = 0
        visited = set()
        flag = False

        def dfs(row, col):
            nonlocal perimeter
            if row < 0 or row >= len(grid) or col < 0 or col >= len(grid[0]) or grid[row][col] == 0:
                perimeter += 1
                return
            if (row, col) in visited:
                return
            
            visited.add((row, col))
            for rNei, cNei in [(row + 1, col), (row - 1, col), (row, col + 1), (row, col - 1)]:
                dfs(rNei, cNei)

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 1:
                    dfs(row, col)
                    flag = True
                    break
            if flag:
                break

        return perimeter