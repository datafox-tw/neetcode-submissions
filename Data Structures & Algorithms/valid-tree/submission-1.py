class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        parent = {i: i for i in range(n)}
        rank = {i: 0 for i in range(n)}  # optional

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x, y):
            rx, ry = find(x), find(y)
            if rx == ry:
                return False  # cycle
            # union by rank (optional)
            if rank[rx] < rank[ry]:
                parent[rx] = ry
            elif rank[rx] > rank[ry]:
                parent[ry] = rx
            else:
                parent[ry] = rx
                rank[rx] += 1
            return True

        if len(edges) != n - 1:
            return False
        for x, y in edges:
            if not union(x, y):
                return False
        return True
