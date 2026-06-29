class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        #loop through the grid. When 1 encountered, run DFS and add each 1 to the visited set
        #Increment numIslands, continue looping until all 1s are visited.

        visited = set()
        numOfIslands = 0

        def dfs(r, c):
            if r < 0 or r >= len(grid) or c < 0 or c >= len(grid[0]) or grid[r][c] == "0" or (r, c) in visited:
                return 0

            visited.add((r, c))
            for row, col in [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)]:
                dfs(row, col)
            return 1

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                numOfIslands += dfs(r, c)

        return numOfIslands