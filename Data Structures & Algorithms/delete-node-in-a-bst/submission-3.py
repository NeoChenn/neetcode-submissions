# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        def dfs(node):
            if not node:
                return None
            if node.val == key:
                if not node.left: return node.right
                if not node.right: return node.left
                # two children — find smallest in right subtree
                slc = node.right
                while slc.left:
                    slc = slc.left
                node.right = self.deleteNode(node.right, slc.val)
                slc.left = node.left
                slc.right = node.right
                return slc
            elif key < node.val:
                node.left = dfs(node.left)
            else:
                node.right = dfs(node.right)
            return node

        return dfs(root)