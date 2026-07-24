class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        adjList = {}
        if not edges:
            return [0]
        for v1, v2 in edges:
            if v1 not in adjList:
                adjList[v1] = []
            if v2 not in adjList:
                adjList[v2] = []
            adjList[v1].append(v2)
            adjList[v2].append(v1)

        def findHeight(n, prev):
            h = 0
            for nei in adjList[n]:
                if nei != prev:
                    h = max(h, 1 + findHeight(nei, n))
            return h

        res = []
        minHeight = len(edges) + 1

        for i in range(n):
            height = findHeight(i, i)  
            if height == minHeight:
                res.append(i)
            elif height < minHeight:
                minHeight = height
                res = []
                res.append(i)

        return res
            