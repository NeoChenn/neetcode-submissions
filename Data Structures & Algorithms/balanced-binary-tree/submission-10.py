# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        #output whether the left and right subtrees of every node differ in height by no more than 1
        
        #1. Define recursive height function, use it on the children of each node, 
        #   return true if the heights differ by no more than 1 
        #   Time complexity of O(N^2)

        self.isBal = True

        def dfs(node):
            if not node:
                return 0

            left = dfs(node.left)
            right = dfs(node.right)
            if abs(left - right) > 1:
                self.isBal = False 
            return 1 + max(left, right) 
            
        dfs(root)
        return self.isBal