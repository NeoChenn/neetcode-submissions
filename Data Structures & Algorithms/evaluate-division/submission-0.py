class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        """
        create adjList with the characters as nodes {letter : [[nei, value]...]}
        use DFS and backtracking to go from query[0] to query[1]
        keep track of an attempt list during traversal, where the value is appended
        if query[1] reached, append all attempt list values multiplied to the res list
        O(number of queries * edges)
        """

        adjList = {}
        for i in range(len(equations)):
            if equations[i][0] not in adjList:
                adjList[equations[i][0]] = []
            if equations[i][1] not in adjList:
                adjList[equations[i][1]] = []
            adjList[equations[i][0]].append([equations[i][1], values[i]])
            adjList[equations[i][1]].append([equations[i][0], 1 / values[i]])
        
        res = []
        attempt = []
        
        def dfs(node, end, prev):
            if node == end:
                total = 1
                for val in attempt:
                    total *= val
                return total

            for nei, val in adjList[node]:
                if nei == prev:
                    continue
                attempt.append(val)
                total = dfs(nei, end, node)
                if total > -1:
                    return total
                attempt.pop()
            return -1

        for query in queries:
            attempt = []
            if query[0] not in adjList or query[1] not in adjList:
                res.append(-1)
            elif query[0] == query[1]:
                res.append(1)
            else: 
                res.append(dfs(query[0], query[1], None))
        
        return res