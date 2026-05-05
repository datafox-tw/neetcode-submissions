class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        from collections import deque
        if not root:
            return 0
        start = root
        q = deque([start])
        result = 0
        #多一個長度一樣的list不會爆空間複雜度，如果對這個表做的事情和q一樣的話時間複雜度也相同
        max_cost = deque([start.val])
        while q:
            qlen = len(q)
            for _ in range(qlen):
                node = q.popleft()
                path_max_cost = max_cost.popleft()
                if node.val >= path_max_cost:
                    result += 1
                current_max = max(path_max_cost, node.val)

                if node.left:
                    q.append(node.left)
                    max_cost.append(current_max)
                if node.right:
                    q.append(node.right)
                    max_cost.append(current_max)
        return result