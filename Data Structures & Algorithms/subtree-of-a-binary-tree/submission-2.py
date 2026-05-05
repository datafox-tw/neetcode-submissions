# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        self.newroots = []
        def find_root_inorder(node):
            if not node:
                return 0
            find_root_inorder(node.left)
            if node.val == subRoot.val:
                self.newroots.append(node)
            find_root_inorder(node.right)
        find_root_inorder(root)
        if len(self.newroots) == 0:
            return False
        self.p_ls = []
        def inorder(node,ls):
            if not node:
                ls.append("Null")
                return 0
            inorder(node.left, ls)
            ls.append(node.val) 
            inorder(node.right, ls)
        inorder(subRoot, self.p_ls)
        self.final_flag = False
        for newroot in self.newroots:
            self.q_ls = []
            inorder(newroot, self.q_ls)
            if self.p_ls == self.q_ls:
                return True
        return False

