class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adjList = {}
        for i in range(n):
            adjList[i] = []
        for a, b in edges:
            adjList[a].append(b)
            adjList[b].append(a)

        visited = set()
        ccs = 0

        def dfs(node):
            if node in visited:
                return
            
            visited.add(node)
            for neighbour in adjList[node]:
                dfs(neighbour)

        for i in range(n):
            if i not in visited:
                dfs(i)
                ccs += 1

        return ccs