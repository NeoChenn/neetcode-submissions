class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        """
        a tree has no cycles and is fully connected
        to check for cycles in undirected graph:
            keep a visited set of nodes, and update after getting to each node
            if next node is visited (ignore parent node), there is a cycle
        to check if fully connected, len(visited) == n at the end
        """
        adjList = {i : [] for i in range(n)}
        for i, j in edges:
            adjList[i].append(j)
            adjList[j].append(i)
        
        visited = set()
        def dfs(node, par):
            if node in visited:
                return False
            visited.add(node)
            for nei in adjList[node]:
                if nei != par:
                    if not dfs(nei, node):
                        return False
            return True
            
        res = dfs(0, -1)
        if len(visited) != n or not res:
            return False
        return True