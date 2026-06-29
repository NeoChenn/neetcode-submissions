# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        self.res = None
        self.found = False
        #bottom-up approach. if node.val == p or node.val == q, return True. 
        #first node where left and right True or its value is p or q and either left and right true

        def dfs(node):
            if not node:
                return False

            left = dfs(node.left)
            right = dfs(node.right)

            if (not self.found) and ((left and right) or ((node.val == p.val or node.val == q.val) and (left or right))):
                self.res = node
                self.found = True
                return False
            
            if node.val == p.val or node.val == q.val or left or right:
                return True

            return False
        
        dfs(root)
        return self.res
