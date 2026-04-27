class StockSpanner:

    def __init__(self):
        self.s = [(-1, float('inf'))]
        self.l = 0

    def next(self, price: int) -> int:
        ref = 0
        while self.s and self.s[-1][-1] <= price:
            self.s.pop()
        if self.s:
            ref = self.l-self.s[-1][0]
        self.s.append((self.l, price))
        self.l += 1
        return ref
        


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)