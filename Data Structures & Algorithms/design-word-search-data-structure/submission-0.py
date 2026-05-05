class TrieNode:
    def __init__(self):
        self.children = dict()
        self.is_end = False
class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end = True

    def search(self, word: str) -> bool:
        print("search: ", word)
        def inner_search(node, idx):
            if idx == len(word):
                return node.is_end
            
            char = word[idx]
            if char != ".":
                if char not in node.children:
                    return False
                return inner_search(node.children[char], idx + 1)
            else:
                for key in node.children:
                    if inner_search(node.children[key], idx + 1):
                        return True
                return False
        
        return inner_search(self.root, 0)