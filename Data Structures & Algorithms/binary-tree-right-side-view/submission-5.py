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
            for i in range(qlen):
                node = q.popleft()
                v = node.val
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            result.append(v)
        return result