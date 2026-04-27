class StockSpanner:

    def __init__(self):
        self.ind = 0
        self.stack = [(-1, float('inf'))]
        

    def next(self, price: int) -> int:
        res = 1
        while self.stack and self.stack[-1][1] <= price:
            self.stack.pop()
        if self.stack:
            res = self.ind-self.stack[-1][0]
        self.stack.append((self.ind, price))
        self.ind += 1
        return res
            
        


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)