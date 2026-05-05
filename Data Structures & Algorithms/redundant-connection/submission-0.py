class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        parent = {i: i for i in range(1,len(edges)+1)}

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        def union(x, y):
            rx, ry = find(x), find(y)
            if rx == ry:
                self.result = [x,y]
            parent[rx] = ry
        for x, y in edges:
            union(x, y)
        return self.result
