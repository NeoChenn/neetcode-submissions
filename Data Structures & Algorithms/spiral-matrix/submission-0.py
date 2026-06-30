class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        self.currDir = 0
        visited = set()
        res = []

        def dfs(r, c):
            if len(res) == len(matrix) * len(matrix[0]):
                return
            
            res.append(matrix[r][c])
            visited.add((r, c))

            nextR = r + dirs[self.currDir][0]
            nextC = c + dirs[self.currDir][1]
            if nextR < 0 or nextR >= len(matrix) or nextC < 0 or nextC >= len(matrix[0]) or (nextR, nextC) in visited:
                if self.currDir == 3:
                    self.currDir = 0
                else:
                    self.currDir += 1
            dfs(r + dirs[self.currDir][0], c + dirs[self.currDir][1])

        dfs(0, 0)
        return res
