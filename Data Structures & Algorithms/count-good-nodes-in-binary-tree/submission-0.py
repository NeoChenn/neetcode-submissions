# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return 0

        self.count = 0

        def dfs(node, highestInPath):
            if not node:
                return 
            if node.val >= highestInPath:
                self.count += 1
                left = dfs(node.left, node.val)
                right = dfs(node.right, node.val)
            else:
                left = dfs(node.left, highestInPath)
                right = dfs(node.right, highestInPath)

        dfs(root, -101)
        return self.count
