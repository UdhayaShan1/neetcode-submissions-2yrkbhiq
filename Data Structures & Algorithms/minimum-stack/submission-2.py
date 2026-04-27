class MinStack:

    def __init__(self):
        self.s = []
        self.ms = []
        

    def push(self, val: int) -> None:
        self.s.append(val)
        if not self.ms:
            self.ms.append(val)
        else:
            self.ms.append(min(val, self.ms[-1]))
        

    def pop(self) -> None:
        self.s.pop()
        self.ms.pop()
        

    def top(self) -> int:
        return self.s[-1]
        

    def getMin(self) -> int:
        return self.ms[-1]
        
