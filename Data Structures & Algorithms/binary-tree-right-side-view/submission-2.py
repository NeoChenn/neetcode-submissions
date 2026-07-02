# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        #BFS on tree
        if not root:
            return []

        res = []
        q = deque([root])
        while q:
            lenSnapshot = len(q)
            for i in range(lenSnapshot):
                curr = q.popleft()  
                if i == lenSnapshot - 1:
                    res.append(curr.val)
                if curr.left:
                    q.append(curr.left)
                if curr.right:
                    q.append(curr.right)
        
        return res
                