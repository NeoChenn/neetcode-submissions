# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        def dfs(node):
            if node == None:
                return False
            
            if node.val == subRoot.val and compareTrees(node, subRoot):
                return True
        
            left = dfs(node.left)
            right = dfs(node.right)
            return left or right

        def compareTrees(node, subnode):
            if not node and not subnode:
                return True
            if not node or not subnode or node.val != subnode.val:
                return False
            
            left = compareTrees(node.left, subnode.left)
            right = compareTrees(node.right, subnode.right)
            return left and right

        return dfs(root)