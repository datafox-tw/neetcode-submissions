class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.ans = float("-inf")

        def dfs(node):
            if not node:
                return 0

            left_gain = max(0, dfs(node.left))
            right_gain = max(0, dfs(node.right))

            # 以 node 當「拐點」的路徑（左右都可以接）
            self.ans = max(self.ans, node.val + left_gain + right_gain)

            # 回傳給 parent：只能選一邊接上去
            return node.val + max(left_gain, right_gain)

        dfs(root)
        return self.ans
