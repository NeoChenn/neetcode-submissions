# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        def dfs(node, isBalanced):
            if not node:
                return [0, True]

            left = dfs(node.left, isBalanced)
            right = dfs(node.right, isBalanced)

            if abs(left[0] - right[0]) > 1 or not left[1] or not right[1]:
                isBalanced = False

            return [1 + max(left[0], right[0]), isBalanced]

        return dfs(root, True)[1]