class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        """
        Way 1: For each node, find height and add to array. Sort and return the smallest(s)
        O(n^2)
        """
        if not edges:
            return [0]

        adjList = {}
        for a, b in edges:
            if a not in adjList:
                adjList[a] = []
            if b not in adjList:
                adjList[b] = []
            adjList[a].append(b)
            adjList[b].append(a)

        res = []
        def findHeight(node, prevNode):
            
            maxNeiHeight = 0
            for nei in adjList[node]:
                if nei != prevNode:
                    maxNeiHeight = max(maxNeiHeight, findHeight(nei, node))

            return 1 + maxNeiHeight
        
        for node in range(n):
            res.append([findHeight(node, -1), node])

        res.sort()
        min_height = res[0][0]
        return [node for height, node in res if height == min_height]