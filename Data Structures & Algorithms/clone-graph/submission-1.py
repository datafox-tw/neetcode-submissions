class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        visited = {}
        
        def dfs(node):
            if node in visited:
            # 如果已經建立過node就不用重新建立，把新的node回傳回去
                return visited[node]
            
            # 1.因為是deepcopy所以要把每個Node都建起來，每個Node的val跟adjancent list構築
            # 2.但是應該不需要完全照者1->2->3走，只要一開始的node對，後面每個node的val跟adjancent list相同就好
            # 3.如果這個node還沒有看過，那就新建立一個node元件
            copy = Node(node.val)
            # 4. 有了value之後還要adjancent list
            # 只是這個visited變成舊node->新node的對應用在一開始的檢測不太習慣
            visited[node] = copy
            for neighbor in node.neighbors:
			          # 把adjancent node也加進去（neighbor裝的不只是編號而是一個完整的node)
                copy.neighbors.append(dfs(neighbor))
            return copy

        if node:
            return dfs(node)
        else:
            return None