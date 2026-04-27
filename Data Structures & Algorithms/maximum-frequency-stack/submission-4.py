class FreqStack:

    def __init__(self):
        self.maxf = 0
        self.f = {}
        self.count = {}
        

    def push(self, val: int) -> None:
        self.count[val] = self.count.get(val, 0)+1
        new_freq = self.count[val]
        if new_freq not in self.f:
            self.f[new_freq] = []
        self.f[new_freq].append(val)
        self.maxf = max(self.maxf, new_freq)


        

    def pop(self) -> int:
        ans = self.f[self.maxf].pop()
        if len(self.f[self.maxf]) == 0:
            del self.f[self.maxf]
            self.maxf -= 1
        self.count[ans] -= 1
        if self.count[ans] == 0:
            del self.count[ans]
        return ans
        


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()