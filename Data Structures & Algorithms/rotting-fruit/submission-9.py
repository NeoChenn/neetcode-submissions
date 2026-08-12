class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        """
        traverse through grid and add rotten fruits to priority queue for BFS
        increment time after each "spread of rotting"
        traverse through grid and return minutes if no fresh fruits, otherwise return -1

        to avoid 2nd grid traverse, count fresh fruits on first traverse
        and decrement in the BFS
        if fresh fruits == 0, return minutes. Otherwise return -1
        """

        minutes = 0
        freshFruits = 0
        q = deque()

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 2:
                    q.append((r, c))
                elif grid[r][c] == 1:
                    freshFruits += 1
                
        if not q and freshFruits == 0:
            return 0

        while q:
            for _ in range(len(q)):
                r, c = q.popleft()
                for rNei, cNei in [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)]:
                    if rNei < 0 or cNei < 0 or rNei >= len(grid) or cNei >= len(grid[0]) or grid[rNei][cNei] != 1:
                        continue
                    q.append((rNei, cNei))
                    grid[rNei][cNei] = 2
                    freshFruits -= 1
            minutes += 1

        if freshFruits == 0:
            return minutes - 1
        else:
            return -1
