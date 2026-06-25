class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        #multi-source bfs twice. From nodes adj to atlantic and from adj to pacific ocean
        #if there is overlap in the two visited sets, add that cell to results.

        res = []
        pacVisited = set()
        atlVisited = set()
        q = deque()

        def isValidNeighbour(r, c, visited):
            return (r >= 0 and r < len(heights) and c >= 0 and c < len(heights[0]) and (r, c) not in visited)

        #starting from pacific
        for row in range(len(heights)):
            q.append((row, 0))
            pacVisited.add((row, 0))
        for col in range(1, len(heights[0])):
            q.append((0, col))
            pacVisited.add((0, col))
        
        while q:
            cRow, cCol = q.popleft()
            neighbours = [(cRow + 1, cCol), (cRow - 1, cCol), (cRow, cCol + 1), (cRow, cCol - 1)]
            for nRow, nCol in neighbours:
                if isValidNeighbour(nRow, nCol, pacVisited) and heights[cRow][cCol] <= heights[nRow][nCol]:
                    q.append((nRow, nCol))
                    pacVisited.add((nRow, nCol))

        q.clear()

        #moving onto atlantic
        for row in range(len(heights)):
            q.append((row, len(heights[0]) - 1))
            atlVisited.add((row, len(heights[0]) - 1))
        for col in range(len(heights[0]) - 1):
            q.append((len(heights) - 1, col))
            atlVisited.add((len(heights) - 1, col))
        
        while q:
            cRow, cCol = q.popleft()
            neighbours = [(cRow + 1, cCol), (cRow - 1, cCol), (cRow, cCol + 1), (cRow, cCol - 1)]
            for nRow, nCol in neighbours:
                if isValidNeighbour(nRow, nCol, atlVisited) and heights[cRow][cCol] <= heights[nRow][nCol]:
                    q.append((nRow, nCol))
                    atlVisited.add((nRow, nCol))

        for r, c in pacVisited:
            if (r, c) in atlVisited:
                res.append([r, c])

        return res