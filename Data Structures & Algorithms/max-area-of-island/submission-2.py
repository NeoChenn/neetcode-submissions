class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        visited = set()
        maxArea = 0

        def dfs(r, c):
            if r < 0 or r >= len(grid) or c < 0 or c >= len(grid[0]) or (r, c) in visited or grid[r][c] == 0:
                return 0

            visited.add((r, c))
            return 1 + dfs(r + 1, c) + dfs(r - 1, c) + dfs(r, c + 1) + dfs(r, c - 1)

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                maxArea = max(maxArea, dfs(r, c))

        return maxArea

