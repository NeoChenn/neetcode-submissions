# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left 
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        """
        recursively traverse tree using DFS
        starting from root, we decide to take or skip the current node
        if we take, we must skip the children
        if we skip, we can either take, or skip each of the children
        return maximum taken
        """
        cache = {}

        def dfs(node, canTake):
            if not node:
                return 0
            if (node, canTake) in cache:
                return cache[(node, canTake)]
            
            take = 0
            if canTake:
                take = node.val + dfs(node.left, False) + dfs(node.right, False)
            skip = dfs(node.left, True) + dfs(node.right, True)
            cache[(node, canTake)] = max(take, skip)
            return cache[(node, canTake)]

        return dfs(root, True)