# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        #from smallest to largest. left, mid, right
        self.arr = []

        def dfs(node):
            if not node:
                return

            if len(self.arr) > k:
                return

            left = dfs(node.left)
            self.arr.append(node.val)
            right = dfs(node.right)

        dfs(root)
        return self.arr[k-1]