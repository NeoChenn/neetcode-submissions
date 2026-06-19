# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res = 0

        def height(node):
            nonlocal res
            if node is None:
                return 0
            left = height(node.left)
            right = height(node.right)
            res = max(res, left + right)  # update diameter at each node
            return 1 + max(left, right)   # return height to parent

        height(root)
        return res