# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = [] #values of node that are last in the queue per level
        if not root:
            return []
        q = deque([root])

        while q:
            lenq = len(q)
            for i in range(lenq):
                curr = q.popleft()
                if i == lenq - 1:
                    res.append(curr.val)
                if curr.left:
                    q.append(curr.left)
                if curr.right:
                    q.append(curr.right)

        return res
