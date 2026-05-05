class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.maxsum = -99999
        def dfs(node):
            if not node:
                return 0

            left_gain = max(dfs(node.left),0)
            right_gain = max(dfs(node.right),0)

            # 左中右誰最大？還是左右都很爛就都不要(中：把左邊和右邊連起來)
            self.maxsum = max(self.maxsum, left_gain+right_gain+node.val)
            print("left: ", left_gain)
            print("right: ", right_gain)
            print("node.val: ", node.val)
            print(self.maxsum)
            print("!!!")
            return node.val+max(left_gain, right_gain)
        if root:
            dfs(root)
        return self.maxsum
