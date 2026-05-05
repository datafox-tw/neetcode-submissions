# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:

    # Encodes a tree to a single string.最簡單的方法就是做中->左->右的preorder traversal然後帳他變成string
    def serialize(self, root: Optional[TreeNode]) -> str:
        if not root:
            return "Null" #隨便一組英文字就好
        res = []
        queue = deque([root])
        while queue:
            node = queue.popleft()
            if not node:
                res.append("Null") 
            else:
                res.append(str(node.val))
                queue.append(node.left)
                queue.append(node.right)
        return ",".join(res) #用逗點來分隔每個符號之後可以用來定位

    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        vals = data.split(",")
        if vals[0] == "Null":
            return None
        root = TreeNode(int(vals[0]))
        queue = deque([root])
        index = 1
        while queue:
            node = queue.popleft()
            if vals[index] != "Null":
                node.left = TreeNode(int(vals[index]))
                queue.append(node.left)
            index += 1
            if vals[index] != "Null":
                node.right = TreeNode(int(vals[index]))
                queue.append(node.right)
            index += 1
        return root