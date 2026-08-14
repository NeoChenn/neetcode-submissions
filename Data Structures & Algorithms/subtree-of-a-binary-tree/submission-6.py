# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        """
            traverse root until we find the root of the subroot
            check for equality starting at the newfound root of the root and the root of the subroot
        """
        def isEqual(root1, root2):
            if not root1 and not root2:
                return True
            elif not root1 or not root2:
                return False

            left = isEqual(root1.left, root2.left)
            right = isEqual(root1.right, root2.right)

            return left and right and root1.val == root2.val

        def dfs(node):
            if not node:
                return None

            if node.val == subRoot.val:
                if isEqual(node, subRoot):
                    return True
            
            left, right = dfs(node.left), dfs(node.right)
            if left != None:
                return left
            if right != None:
                return right
            return None
        
        res = dfs(root)
        if res == None:
            return False
        return res

        