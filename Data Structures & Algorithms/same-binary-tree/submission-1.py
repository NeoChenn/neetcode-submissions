# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        parr = []
        qarr = []

        def dfs(node, arr):
            if node == None:
                arr.append(None)
                return
            
            arr.append(node.val)
            dfs(node.left, arr)
            dfs(node.right, arr)

        dfs(p, parr)
        dfs(q, qarr)
        if parr == qarr:
            return True
        return False

