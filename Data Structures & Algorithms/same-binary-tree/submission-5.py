# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        self.isSame = True
        def dfs(pNode, qNode):

            if pNode == None and qNode == None:
                return
            
            elif pNode == None or qNode == None:
                self.isSame = False
                return

            if pNode.val != qNode.val:
                self.isSame = False
                return

            dfs(pNode.left, qNode.left)
            dfs(pNode.right, qNode.right)

        dfs(p, q)
        return self.isSame