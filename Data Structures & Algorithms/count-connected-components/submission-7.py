class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        parent = {i: i for i in range(n)}
        # 1) parent 陣列，一開始每個點都是自己的老大
        rank = {i: 0 for i in range(n)}  # optional
        # 2) find(x)：找 x 所屬集合的老大，代表自己這坨人
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        # 3) union(x, y)：把兩個集合合起來
        for x, y in edges:
            rx, ry = find(x), find(y)
            #這題就算有cycle也沒差
            #總是用value比較小的那邊當頭? ->不一定主因是最後還要再find各自的老大一次（很明顯）

            parent[rx] = ry
        return len({find(i) for i in range(n)})

