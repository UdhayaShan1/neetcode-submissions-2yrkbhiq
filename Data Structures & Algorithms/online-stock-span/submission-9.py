class StockSpanner:

    def __init__(self):
        self.s = [float('inf')]
        self.stack = [0]
        self.ind = 1
        

    def next(self, price: int) -> int:
        ans = 1
        while self.stack and self.s[self.stack[-1]] <= price:
            self.stack.pop()
        if self.stack:
            ans = self.ind-self.stack[-1]
        self.stack.append(self.ind)
        self.s.append(price)
        self.ind += 1
        return ans

        


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)