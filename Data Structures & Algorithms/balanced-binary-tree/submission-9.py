# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        #calculate height of node
        #if difference between height of node.left and node.right > 1, return False
        self.isBal = True

        def dfs(node):
            if node == None:
                return 0
            
            left = 1 + dfs(node.left)
            right = 1 + dfs(node.right)

            if abs(left - right) > 1:
                self.isBal = False

            return max(left, right)

        dfs(root)
        if self.isBal:
            return True
        return False