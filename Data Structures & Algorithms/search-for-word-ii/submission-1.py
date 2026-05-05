class TrieNode:
    def __init__(self):
        self.word = ""
        self.children = dict() # dict[str] : "TrieNode"
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        # first step:建立tries
        # 有一個空的root然後把幾個word都塞到trienodes裡面

        # 記得初始化時要initialize root這個trienode
        self.root = TrieNode()
        for w in words:
            node = self.root
            for char in w:
                if char not in node.children: #第一個node時，node.children是空的
                    node.children[char] = TrieNode()
                node = node.children[char]
            node.word = w
        # second step:把原本的word search搞來然後進行處理
        R, C = len(board), len(board[0])
        dirs = [(0,1),(0,-1),(1,0),(-1,0)]
        result = []
        # 但是這題的word search有點backtrack的味道，因為結構不太一樣，cat和cart都要在a後面進行搜索
        def dfs(r: int, c: int, node:Optional["TrieNode"]) -> bool:
            # thought:每次檢查的格子，不管是第一層root還是後面的幾層，要馬屬於children其中一種要馬不是
            block_val = board[r][c]
            if block_val not in node.children:
                return
            # 如果有的話就是使用這個點然後看這個點的小孩然後向下延伸
            next_node = node.children[block_val]
            # 早停條件：來到終點
            if len(next_node.word) >0:
                result.append(next_node.word)
                # 因為有back跟backpack這種情況所以還不能停止
                # 去重：這個點有找到過之後就不鳥他了
                next_node.word = ""
            # 先暫時把這個點標為marked，之後沒有要選再搞回來（和backtracking像）
            board[r][c] = "#"
            for dr,dc in dirs:
                nr, nc = r + dr, c + dc # new橫軸縱軸
                if 0 <= nr < R and 0 <= nc < C and board[nr][nc] != "#":
                    #代表可以嘗試這格
                    dfs(nr, nc, node.children[block_val])
            board[r][c] = block_val
        for i in range(R):
            for j in range(C):
                dfs(i, j, self.root) # root = 第0層，語意也比較乾淨
        return result
