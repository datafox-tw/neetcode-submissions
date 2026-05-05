# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        from collections import deque
        if not root:
            return []
        start = root
        q = deque([start])
        result = []
        while q:
            qlen = len(q)
            level = []
            for i in range(qlen):
                node = q.popleft()
                level.append(node.val)
                #1 ->2 -> 4
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            result.append(level[-1])
        return result