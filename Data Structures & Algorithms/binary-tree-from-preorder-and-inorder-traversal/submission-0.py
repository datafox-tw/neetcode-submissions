# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # 為了 O(1) 查 index
        idx_map = {val: i for i, val in enumerate(inorder)}

        def helper(pre_l, pre_r, in_l, in_r):
            if pre_l > pre_r:
                return None

            root_val = preorder[pre_l]
            root = TreeNode(root_val)

            in_root_idx = idx_map[root_val]
            left_size = in_root_idx - in_l

            root.left = helper(
                pre_l + 1,
                pre_l + left_size,
                in_l,
                in_root_idx - 1
            )

            root.right = helper(
                pre_l + left_size + 1,
                pre_r,
                in_root_idx + 1,
                in_r
            )

            return root

        return helper(0, len(preorder) - 1, 0, len(inorder) - 1)
