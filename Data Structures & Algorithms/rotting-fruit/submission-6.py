class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        #multi-source BFS on each rotten fruit
        #increment minute after each "level"
        #once done, loop through each square and if there are any fresh fruits, return -1

        q = deque()
        self.minutes = 0
        fresh = False

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 2:
                    q.append((r, c))
                elif grid[r][c] == 1 and not fresh:
                    fresh = True

        if not fresh:
            return 0

        def bfs():
            while q:
                for _ in range(len(q)):
                    r, c = q.popleft()

                    for row, col in [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)]:
                        if not (row < 0 or row >= len(grid) or col < 0 or col >= len(grid[0]) or grid[row][col] != 1):
                            q.append((row, col))
                            grid[row][col] = 2
                self.minutes += 1

        bfs()
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    return -1
        return self.minutes - 1
