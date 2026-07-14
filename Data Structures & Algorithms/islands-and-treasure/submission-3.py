class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        q = deque()
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 0:
                    q.append((r, c))

        level = 0
        while q:
            for i in range(len(q)):
                currRow, currCol = q.popleft()
                
                for r, c in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    newRow, newCol = currRow + r, currCol + c
                    if 0 <= newRow < len(grid) and 0 <= newCol < len(grid[0]) and grid[newRow][newCol] == 2147483647:
                        grid[newRow][newCol] = level + 1  # mark immediately when enqueuing
                        q.append((newRow, newCol))
            level += 1