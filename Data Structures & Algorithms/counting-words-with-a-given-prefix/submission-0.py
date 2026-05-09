class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        class Node:
            def __init__(self):
                self.children = {}
                self.count = 0
        
        class Trie:
            def __init__(self):
                self.root = Node()
            def insert(self, word):
                root = self.root
                for ch in word:
                    if ch not in root.children:
                        root.children[ch] = Node()
                    
                    root = root.children[ch]
                    root.count += 1
            def search(self, word):
                root = self.root
                for ch in word:
                    if ch not in root.children:
                        return 0
                    root = root.children[ch]
                return root.count
        t = Trie()

        for i in words:
            t.insert(i)
        return t.search(pref)
                    