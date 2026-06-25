class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        #no loops and fully connected.
        #check for loops ONCE starting from one node. 
        #if any node not in visited set or loop is found, return false
        #As opposed to directed graphs, no path here.
        #Path needed in di as two routes to same destination not necessarily a cycle
        #A → B
        #A → C → B
        #but in undirected, it is 100% a cycle

        adjList = {}
        for i in range(n):
            adjList[i] = []
        for node1, node2 in edges:
            adjList[node1].append(node2)
            adjList[node2].append(node1)

        visited = set()
        
        def dfs(curr, parent):
            if curr in visited:
                return False

            visited.add(curr)
            for neighbor in adjList[curr]:
                if neighbor != parent:
                    if not dfs(neighbor, curr):
                        return False
            return True
            

        if not dfs(0, None) or len(visited) != n:
            return False
        return True