# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        count = 0
        def preorder(node, maximum):
            nonlocal count
            if not node:
                return
            
            if node.val >= maximum:
                count += 1

            left = preorder(node.left, max(maximum, node.val))
            right = preorder(node.right, max(maximum, node.val))

        preorder(root, -101)
        return count