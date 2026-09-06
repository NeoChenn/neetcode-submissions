# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        #find node. if node has
        #no children, delete itself by having parents point at none
        #one child, link parent with child
        #if two childs, replace with smallest larger child or largest smaller child

        """
        recursive function returns node
        """
        def dfs(node):
            if not node or (node.val == key and not node.left and not node.right):
                return None
            if node.val == key and (not node.left or not node.right):
                if node.left:
                    return node.left
                else:
                    return node.right
            if node.val == key and node.left and node.right:
                """
                find smallest larger child SLC (which either has no children, or a bigger child)
                replace:
                    have a pointer to the SLC
                    remove it with deleteNode()
                    transfer nodes' children to SLC's children
                    return SLC
                """
                slc = node.right
                while slc.left:
                    slc = slc.left
                self.deleteNode(root, slc.val)
                slc.left, slc.right = node.left, node.right
                node.left, node.right = None, None
                return slc
            node.left = dfs(node.left)
            node.right = dfs(node.right)
            return node
        return dfs(root)