"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        #node is the first node in the graph, and has 1 as the value
        #dfs through each of the non-visited neighbors, marking itself as visited
        if not node:
            return

        oldToNew = {}

        def dfs(node):
            if node in oldToNew:
                return oldToNew[node]  # return existing clone
            
            clone = Node(node.val)
            oldToNew[node] = clone
            for neighbor in node.neighbors:
                clone.neighbors.append(dfs(neighbor))  # append cloned neighbor
            return clone

        return dfs(node)