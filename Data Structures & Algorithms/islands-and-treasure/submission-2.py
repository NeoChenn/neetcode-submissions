class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:

        visited = set()
        q = deque()

        def isNeighbourValid(row, col):
            if row < 0 or row >= len(grid) or col < 0 or col >= len(grid[1]) or (row, col) in visited or grid[row][col] == -1:
                return False
            return True

        def bfs(row, col): #params of a land cell that can be traversed
            q.append((row, col))
            visited.add((row, col))
            dist = 0

            while q:
                for _ in range(len(q)): 
                    curr = q.popleft()
                    neighbors = [(curr[0] + 1, curr[1]), (curr[0] - 1, curr[1]), (curr[0], curr[1] + 1), (curr[0], curr[1] - 1)]
                    for r, c in neighbors:
                        if isNeighbourValid(r, c):
                            if grid[r][c] == 0:
                                return dist + 1
                            q.append((r, c))
                            visited.add((r, c))
                dist += 1
            return float('inf')

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 2147483647:
                    grid[row][col] = bfs(row, col)
                    visited.clear()
                    q.clear()