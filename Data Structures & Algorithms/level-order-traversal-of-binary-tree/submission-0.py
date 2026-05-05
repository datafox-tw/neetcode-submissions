# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        #應該是不一定全滿，所以我們要用某種方式保留層級敢，也就是用qlen的方式
        #每次到新的一層, q裡面的東西都不一樣
        # ex. 第一層只有1
        # ex. 第二層有23
        #第三層有4567...
        #每次q中都是把這層的內容結束掉換下一層的東西
        from collections import deque
        if not root:
            return []
        start = root
        q = deque([start])
        result = []
        while q:
            qlen = len(q)
            level = []
            for i in range(qlen):
                node = q.popleft()
                level.append(node.val)
                #1 ->2 -> 4
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            result.append(level)
        return result