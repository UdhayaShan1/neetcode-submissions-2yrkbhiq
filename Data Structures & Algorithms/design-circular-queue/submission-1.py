class Node:
    def __init__(self, val):
        self.val = val
        self.nxt = None
        self.prev = None

class MyCircularQueue:

    def __init__(self, k: int):
        self.head = None
        self.tail = None
        self.length = 0
        self.cap = k
        

    def enQueue(self, value: int) -> bool:
        if self.length == 0:
            self.head = Node(value)
            self.tail = self.head
            self.tail.nxt = self.head
            self.length += 1
            return True
        else:
            if self.length < self.cap:
                ref = Node(value)
                self.tail.nxt = ref
                ref.nxt = self.head
                self.tail = ref
                self.length += 1
                return True
            else:
                return False
        
        
    def deQueue(self) -> bool:
        if self.length == 0:
            return False
        if self.length == 1:
            self.head = None
            self.tail = None
            self.length = 0
            return True
        else:
            nxt = self.head.nxt
            self.head = nxt
            self.tail.nxt = nxt
            self.length -= 1
            return True

    def Front(self) -> int:
        return self.head.val if self.head else -1
        

    def Rear(self) -> int:
        return self.tail.val if self.tail else -1
        

    def isEmpty(self) -> bool:
        return self.length == 0
        

    def isFull(self) -> bool:
        return self.length == self.cap
        


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()