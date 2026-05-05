class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        # 使用bst
        from collections import deque
        if not root:
            return 0
        start = root
        q = deque([start])
        result = 0
        #多一個長度一樣的list不會爆空間複雜度，如果對這個表做的事情和q一樣的話時間複雜度也相同
        max_cost = deque([start.val])
        while q:
            node = q.popleft()
            path_max_cost = max_cost.popleft()
            if node.val >= path_max_cost:
                result += 1
            current_max = max(path_max_cost, node.val)

            if node.left:
                q.append(node.left)
                #不管是左子還是右子，從root到他們父親之間的最大節點是一樣的
                max_cost.append(current_max)
            if node.right:
                q.append(node.right)
                max_cost.append(current_max)
        return result