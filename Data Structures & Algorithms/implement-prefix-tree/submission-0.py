class Node:
    def __init__(self):
        self.children  = {}
        self.end = False

class PrefixTree:

    def __init__(self):
        self.root = Node()
        

    def insert(self, word: str) -> None:
        root = self.root
        for ch in word:
            if ch not in root.children:
                root.children[ch] = Node()
            root = root.children[ch]
        root.end = True
        
            


    def search(self, word: str) -> bool:
        root = self.root
        for ch in word:
            if ch not in root.children:
                return False
            root = root.children[ch]
        return root.end

        

    def startsWith(self, prefix: str) -> bool:
        root = self.root
        for ch in prefix:
            if ch not in root.children:
                return False
            root = root.children[ch]
        return True
        