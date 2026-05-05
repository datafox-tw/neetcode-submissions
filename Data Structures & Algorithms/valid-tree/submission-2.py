class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        parent = {i: i for i in range(n)}
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x, y):
            rx, ry = find(x), find(y)
            if rx == ry:
                return False  # cycle
            parent[rx] = ry
            return True

        if len(edges) != n - 1:
            return False
        for x, y in edges:
            if not union(x, y):
                return False
        return True
