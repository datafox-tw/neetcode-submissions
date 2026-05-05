# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        print("root: ", root.val) if root else print("Root: None")
        print("subroot: ", subRoot.val)if subRoot else print("subRoot: None")
        # 這個只有subroot整顆樹是空的才會出現，屬於最最一開始的保險
        if not subRoot:
            return True
        # 這裡是如果已經探索到最下層還沒找到就要false
        if not root:
            return False

        if self.sameTree(root, subRoot):
        #兩個點當root，這兩個點代表兩棵樹的的root(我指的是兩棵樹的原點節點)，檢查這兩棵樹的細節，如果全部一樣就是return true
            return True
        # 重點是subRoot在這邊不會動，因為是大樹、的某個root跟小樹的最上面subroot比較，只要有其中一個符合就好
        # 所以這裡用的是return issubtree(left or right)不是and 
        # 一切都是邏輯
        return (self.isSubtree(root.left, subRoot) or
               self.isSubtree(root.right, subRoot))
        #最上層是1，在這題的例子裡面1左邊2倍if self.sametree那邊return true, 右邊則是被not root回傳false（三的子樹是空的->false->3本身是false)
        #true跟false取or是true

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