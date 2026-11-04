# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        """
         function returns the LCA of p and q
         cases:
            p.val and q.val smaller than node.val, recurse to node.left
            p.val and q.val bigger than node.val, recurse to node.right
            ( p.val or q.val equals node.val ) or (p.val and q.val are at either child), found LCA
        """
        def recursion(node):
            if not node:
                return False

            if p.val < node.val and q.val < node.val:
                res = recursion(node.left)            
                if res:
                    return res
            elif p.val > node.val and q.val > node.val:
                res = recursion(node.right)
                if res:
                    return res
            else:
                return node
                
        return recursion(root)