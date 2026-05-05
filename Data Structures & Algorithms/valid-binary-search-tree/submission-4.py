# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        from collections import deque
        if not root:
            return False
        q = deque([(root,-1001, 1001)])
        while q:
            # 邊bst邊檢查每個node
            node,minval,maxval = q.popleft()
            if not (minval < node.val<maxval):
                return False
            if node.left:
                q.append((node.left,minval,node.val))
            if node.right:
                q.append((node.right,node.val,maxval))
        return True
