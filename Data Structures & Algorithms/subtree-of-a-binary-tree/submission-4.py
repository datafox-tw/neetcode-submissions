# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        self.flag = False
        if not subRoot:
            return True
        def dfs(node):
            if self.flag:
                return 
            if node:
                if self.sameTree(node, subRoot):
                    self.flag = True
                    return
                dfs(node.left)
                dfs(node.right)
        dfs(root)
        return self.flag

    def sameTree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # 一起走到了最下面：return True, ex. 5這個node的left and right都是空的所以return True
        #再往上看 5的這一點就會被驗證，因為self.sametree(left跟right)都是true這樣網上時才是true
        # 如果今天檢查的點不是空值（就是root and subRoot那邊），就是要檢查：
        # 1. 要檢查的node左邊和右邊值是否一樣
        # 2. 他的子結構是否一樣（如果一整顆樹是sametree，那麼他的底下節點都會是sametree)
        # 而且這兩棵樹的遍歷方式也會一樣
        if not root and not subRoot:
            return True
        if root and subRoot and root.val == subRoot.val:
            return (self.sameTree(root.left, subRoot.left) and
                   self.sameTree(root.right, subRoot.right))
        return False