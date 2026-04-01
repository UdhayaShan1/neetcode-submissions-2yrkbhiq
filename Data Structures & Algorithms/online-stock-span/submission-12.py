class StockSpanner:

    def __init__(self):
        self.s = [(float('inf'), -1)]
        self.c = 0

        

    def next(self, price: int) -> int:
        #print(self.s)
        while self.s and self.s[-1][0] <= price:
            self.s.pop()
        res = 1
        if self.s:
            res = self.c - self.s[-1][1]
        self.s.append((price, self.c))
        self.c += 1
        return res


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)