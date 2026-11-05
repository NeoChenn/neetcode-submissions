"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        """
        hashmap {node: clone}
        create a clone of node
        access each neighbour in node
            if clone of neighbour has been created, add it to clone node's neighbours
            else, recurse to the neighbour of node and add clone node's neighbours
        return clone of node
        """
        nodeToClone = {}
        def recursion(node):
            if not node:
                return None
            clone = Node(node.val)
            nodeToClone[node] = clone
            for nei in node.neighbors:
                if nei in nodeToClone:
                    clone.neighbors.append(nodeToClone[nei])
                else:
                    clone.neighbors.append(recursion(nei))
            return clone
        return recursion(node)