class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set()

        self.n = 0
        def dfs(row, col):
            if row < 0 or col < 0 or row >= len(grid) or col >= len(grid[0]) or (row, col) in visited or grid[row][col] == "0":
                return

            visited.add((row, col))
            dfs(row + 1, col)
            dfs(row - 1, col)
            dfs(row, col + 1)
            dfs(row, col - 1)
        
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == "1" and (r, c) not in visited:
                    dfs(r, c)
                    self.n += 1
        
        return self.n