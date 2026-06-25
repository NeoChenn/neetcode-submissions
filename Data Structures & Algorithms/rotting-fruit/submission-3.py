class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        #multi-source BFS
        #Could change grid values in-place from fresh (1) to rotten (2) instead visited set. 
        
        visited = set()
        q = deque()
        minutes = 0
        freshExists = False

        def isValidNeighbor(r, c):
            if r < 0 or r >= len(grid) or c < 0 or c >= len(grid[0]) or grid[r][c] != 1 or (r, c) in visited:
                return False
            return True          
        
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 2:
                    q.append((r, c))
                    visited.add((r, c))
                if grid[r][c] == 1:
                    freshExists = True
        
        if not q and freshExists:
            return -1
        elif not q:
            return 0

        while q:
            for _ in range(len(q)):
                cRow, cCol = q.popleft()
                neighbors = [(cRow + 1, cCol), (cRow - 1, cCol), (cRow, cCol + 1), (cRow, cCol - 1)]
                for nRow, nCol in neighbors:
                    if isValidNeighbor(nRow, nCol):
                        q.append((nRow, nCol))
                        visited.add((nRow, nCol))
            minutes += 1

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1 and (r, c) not in visited:
                    return -1

        return minutes - 1
