# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        """
        We have 5 as the root.                                         in = [3, 2, 1, 5, 6, 4]
        Next 2, which is to the left of the in array so 5.left = 2     in = [3, 2, 1]
        Next 3, which is to the left of 2, so 2.left = 3               in = [3]
        Next 1, which is to the right of 2, so 2.right = 1             in = [1]
        Next 4, which is to the right of 5, so 5.right = 4             in = [6, 4]
        Next 6, which is to the left of 4, so 4.left = 6               in = [6]

        recursive function that returns node
        builds tree in preorder
        
        base case: inorder list length  == 1, we return that node
        preorder = [5, 2, 3, 1, 4, 6]
        inorder = [3, 2, 1, 5, 6, 4]
        """

        inorder_map = {val: i for i, val in enumerate(inorder)}
        index = -1
        def recursion(left, right):
            nonlocal index
            if left > right:
                return None
            index += 1
            val = preorder[index]
            node = TreeNode(val)
            mid = inorder_map[val]
            node.left = recursion(left, mid - 1)
            node.right = recursion(mid + 1, right)
            return node

        return recursion(0, len(inorder) - 1)

        """
        recursion([2, 1, 3, 4]) index = -1
            recursion([2]) index = 0, return node 2
            recursion([3, 4]) index = 1, 
        """