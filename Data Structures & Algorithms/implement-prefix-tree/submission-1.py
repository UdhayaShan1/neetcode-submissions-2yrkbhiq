class Node:
    def __init__(self):
        self.children = {}
        self.end = False

class PrefixTree:

    def __init__(self):
        self.root = Node()
        

    def insert(self, word: str) -> None:
        ref = self.root
        for c in word:
            if c not in ref.children:
                ref.children[c] = Node()
            ref = ref.children[c]
        ref.end = True
        



    def search(self, word: str) -> bool:
        ref = self.root
        for c in word:
            if c not in ref.children:
                return False
            ref = ref.children[c]
        return ref.end

    def startsWith(self, prefix: str) -> bool:
        ref = self.root
        for c in prefix:
            if c not in ref.children:
                return False
            ref = ref.children[c]
        return True

        
        