# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        #Append rightmost node value at every level to res

        if not root:
            return []
        res = [root.val]
        q = deque([root])
        while q:
            qLen = len(q)
            for i in range(qLen):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            if q:
                res.append(q[-1].val)
        return res
