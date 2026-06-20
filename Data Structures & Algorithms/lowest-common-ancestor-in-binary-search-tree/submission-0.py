# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        #compare p and q to curr node
        #if both smaller/bigger, traverse down
        #if one bigger and one smaller, return curr node's value
        #if one equals, return curr node's value

        def dfs(node):
            if node == None:
                return
            if (p.val < node.val and q.val < node.val):
                return dfs(node.left)
            elif (p.val > node.val and q.val > node.val):
                return dfs(node.right)
            else:
                return node


        return dfs(root)