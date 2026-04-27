class StockSpanner:

    def __init__(self):
        self.stack = [(0, float('inf'))]
        self.pos = 1
        

    def next(self, price: int) -> int:
        ref = self.stack
        while ref and ref[-1][1] <= price:
            ref.pop()
        ans = 1
        if ref:
            ans = self.pos-ref[-1][0]
        ref.append((self.pos, price))
        self.pos += 1
        return ans
         


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)