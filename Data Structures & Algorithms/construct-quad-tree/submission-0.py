"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val=False, isLeaf=False, topLeft=None, topRight=None, bottomLeft=None, bottomRight=None):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        """
        pass top left and bottom right coords to "restrict" grid
        if the entire grid is the same, return with isLeaf = 1 and val
        otherwise, recurse through each of the children
        """
        def dfs(node, topLeft, bottomRight):
            val = grid[topLeft[0]][topLeft[1]]
            for row in range(topLeft[0], bottomRight[0] + 1):
                for col in range(topLeft[1], bottomRight[1] + 1):
                    if grid[row][col] != val:
                        #logic for not all equal
                        node.isLeaf, node.val = 0, 0
                        node.topLeft = dfs(Node(), topLeft, ((topLeft[0] + bottomRight[0]) // 2, (topLeft[1] + bottomRight[1]) // 2))
                        node.topRight = dfs(Node(), (topLeft[0], ((topLeft[1] + bottomRight[1]) // 2) + 1), ((topLeft[0] + bottomRight[0]) // 2, bottomRight[1]))
                        node.bottomLeft = dfs(Node(), (((topLeft[0] + bottomRight[0]) // 2) + 1, topLeft[1]), (bottomRight[0], (topLeft[1] + bottomRight[1]) // 2))
                        node.bottomRight = dfs(Node(), (((topLeft[0] + bottomRight[0]) // 2) + 1, ((topLeft[1] + bottomRight[1]) // 2) + 1), bottomRight)
                        return node
            #logic for all equal
            node.isLeaf, node.val = 1, val
            return node

        return dfs(Node(), (0, 0), (len(grid) - 1, len(grid[0]) - 1))