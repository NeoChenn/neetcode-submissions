class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        #no loops and fully connected.
        #check for loops ONCE starting from one node. 
        #if any node not in visited set or loop is found, return false

        adjList = {}
        for i in range(n):
            adjList[i] = []
        for node1, node2 in edges:
            adjList[node1].append(node2)
            adjList[node2].append(node1)

        visited, path = set(), set()
        
        def dfs(curr, parent):
            if curr in path:
                return False
            if curr in visited:
                return True

            path.add(curr)
            for neighbor in adjList[curr]:
                if neighbor != parent:
                    if not dfs(neighbor, curr):
                        return False
            path.remove(curr)
            visited.add(curr)
            return True
            

        if not dfs(0, None) or len(visited) != n:
            return False
        return True