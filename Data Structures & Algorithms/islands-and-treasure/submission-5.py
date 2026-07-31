class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        #multi-source BFS on each treasure chest
        #keep track of the "level" and modify the land cell in-place
        q = deque()

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 0:
                    q.append((r, c))
        
        level = 1
        while q:
            for _ in range(len(q)):
                cur = q.popleft()
                for neiRow, neiCol in [(cur[0] - 1, cur[1]), (cur[0] + 1, cur[1]), (cur[0], cur[1] + 1), (cur[0], cur[1] - 1)]:
                    if neiRow < 0 or neiRow >= len(grid) or neiCol < 0 or neiCol >= len(grid[0]) or grid[neiRow][neiCol] != 2**31 - 1:
                        continue
                    q.append((neiRow,neiCol))
                    grid[neiRow][neiCol] = level                
            level += 1