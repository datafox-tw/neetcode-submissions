class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if not root:
            return None

        # 命中其中一個，直接回傳
        if root.val == p.val or root.val == q.val:
            return root
        # ex. 第一層in 例子2
        # root 是5，左邊是3右邊是8，右邊整體來說會回傳None，左邊回傳3直接卡住，這樣的話return就是3(left)
        #第二個例子：ex 2,4是三
        #第一層：3, 8在這層不會到這邊所以忽略
        #我們在意left的下一層，也就是3當root，看左邊和右邊，因為目前也沒到root=p or root=q
        #在三這個點我繼續走left = self.lca(left), right = lca(right)這裡
        # right就找到了right會return 自己（4）而不是none
        #左邊在這樣找下去也會找到2
        #只有在這個點有
        #最後網上傳遞的時候就看自己是哪邊有哪邊是None回傳有東西的那邊
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        # 兩邊都找到，代表在這層交會
        if left and right:
            return root

        # 只在其中一邊，往上回傳那一邊
        return left if left else right
