class StockSpanner:

    def __init__(self):
        self.stack = [(-1, float('inf'))]
        self.l = 0

    def next(self, price: int) -> int:
        res = 0
        while self.stack and self.stack[-1][1] <= price:
            self.stack.pop()
        if self.stack:
            res = self.l-self.stack[-1][0]
        self.stack.append((self.l, price))

        self.l += 1
        return res
        


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)