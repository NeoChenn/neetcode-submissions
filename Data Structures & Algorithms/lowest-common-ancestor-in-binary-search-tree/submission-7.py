# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        #top down traversal. 
        #compare p and q to curr
        #if one larger and one smaller than curr OR one equals curr, return curr
        #if both larger or both smaller, traverse to subnode that contains both

        def dfs(curr):
            if (p.val < curr.val and q.val < curr.val):
                return dfs(curr.left)
            if (p.val > curr.val and q.val > curr.val):
                return dfs(curr.right)
            return curr
        return dfs(root)