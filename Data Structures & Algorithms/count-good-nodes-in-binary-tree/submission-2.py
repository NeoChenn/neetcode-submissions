# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        #dfs that returns number of good nodes, top-down traversal
        #keep track of highest value found so far
        #if curr.val > highest, return 1 + dfs(...
        #otherwise, return dfs(...

        def dfs(node, highest):
            if not node:
                return 0
            
            if node.val >= highest:
                return 1 + dfs(node.left, node.val) + dfs(node.right, node.val)
            
            return dfs(node.left, highest) + dfs(node.right, highest)

        return dfs(root, -101)

