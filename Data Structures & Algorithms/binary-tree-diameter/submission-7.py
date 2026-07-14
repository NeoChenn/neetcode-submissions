# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        #return longest path between any two nodes
        #for each node, return the longest paths of either subtree added together
        self.longestPath = 0

        def dfs(node):
            if not node:
                return 0

            left = dfs(node.left)
            right = dfs(node.right)
            self.longestPath = max(self.longestPath, left + right)
            return 1 + max(left, right)
            
        dfs(root)
        return self.longestPath