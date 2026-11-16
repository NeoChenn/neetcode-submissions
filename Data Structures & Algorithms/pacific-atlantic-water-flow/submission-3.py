class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        """
        for loop through all the tiles touching the pacific (skipping already visited)
        mark every reachable tile using dfs by adding its coords to a visited set

        do the same with the atlantic with a separate visited set
        if reachable tile reached previously, add coords to res
        
        coords of tiles that touch the pacific: heights[0][c] and heights[r][0]
        coords of tiles that touch the atlantic: heights[-1][c] and heights[r][-1]
        """
        res = []
        pacificVisited = set()
        atlanticVisited = set()

        def pacificDfs(row, col):
            if (row, col) in pacificVisited:
                return
            
            pacificVisited.add((row, col))
            print((row, col))
            for rNei, cNei in [(row + 1, col), (row - 1, col), (row, col + 1), (row, col - 1)]:
                if (rNei >= 0 and rNei < len(heights) and cNei >= 0 and cNei < len(heights[0])) and heights[rNei][cNei] >= heights[row][col]:
                    pacificDfs(rNei, cNei)
        
        for r in range(len(heights)):
            pacificDfs(r, 0)
        for c in range(len(heights[0])):
            pacificDfs(0, c)

        def atlanticDfs(row, col):
            if (row, col) in atlanticVisited:
                return
            
            atlanticVisited.add((row, col))
            print((row, col))
            if (row, col) in pacificVisited:
                res.append([row, col])
            for rNei, cNei in [(row + 1, col), (row - 1, col), (row, col + 1), (row, col - 1)]:
                if (rNei >= 0 and rNei < len(heights) and cNei >= 0 and cNei < len(heights[0])) and heights[rNei][cNei] >= heights[row][col]:
                    atlanticDfs(rNei, cNei)
        
        for r in range(len(heights)):
            atlanticDfs(r, len(heights[0]) - 1)
        for c in range(len(heights[0])):
            atlanticDfs(len(heights) - 1, c)

        return res


