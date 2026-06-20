# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        values = []
        que = deque([root])

        if not root:
            return []

        while que:
            queLen = len(que)
            inLevel = []
            for i in range(queLen):
                node = que.pop()
                inLevel.append(node.val)
                if node.left:
                    que.appendleft(node.left)
                if node.right:
                    que.appendleft(node.right)
        
            values.append(inLevel)

        return values

        #queue [1], [2, 3], [3, 4, 5], [4, 5, 6, 7], [5, 6, 7]
