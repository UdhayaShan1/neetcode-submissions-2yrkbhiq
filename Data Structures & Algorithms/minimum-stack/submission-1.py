class MinStack:

    def __init__(self):
        self.s = []
        self.mins = []
        

    def push(self, val: int) -> None:
        self.s.append(val)
        if len(self.mins) == 0:
            self.mins.append(val)
        else:
            self.mins.append(min(val, self.mins[-1]))
        

    def pop(self) -> None:
        self.mins.pop()
        return self.s.pop()
        

    def top(self) -> int:
        return self.s[-1]
        

    def getMin(self) -> int:
        return self.mins[-1]
        
