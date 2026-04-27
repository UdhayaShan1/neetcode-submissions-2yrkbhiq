class Node:
    def __init__(self, key, value):
        self.k = key
        self.v = value
        self.next = None
        self.prev = None


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.l = 0
        self.map = {}
        self.head = Node(-1, -1)
        self.tail = Node(-1, -1)
        self.head.next = self.tail
        self.tail.prev = self.head
    
    def insert(self, node):
        p = self.tail.prev
        p.next = node
        node.prev = p
        node.next = self.tail
        self.tail.prev = node
        self.l += 1

        if node.k not in self.map:
            self.map[node.k] = node
    
    def remove(self, node):
        #print(node.k, node.v)
        p = node.prev
        nxt = node.next
        p.next = nxt
        nxt.prev = p
        node.prev = None
        node.next = None
        self.l -= 1
        #print(self.map)
        del self.map[node.k]
        


    def get(self, key: int) -> int:
        print(f"Called {key}", self.map)
        if key not in self.map:
            return -1
        node = self.map[key]
        self.remove(node)
        self.insert(node)
        return node.v
        

    def put(self, key: int, value: int) -> None:
        if key not in self.map:
            if self.l == self.capacity:
                self.remove(self.head.next)

            new = Node(key, value)
            self.insert(new)
        else:
            ref = self.map[key]
            ref.v = value
            self.remove(ref)
            self.insert(ref)

            

        
