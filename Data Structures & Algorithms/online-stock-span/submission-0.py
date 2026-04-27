class StockSpanner:

    def __init__(self):
        self.p = []
        

    def next(self, price: int) -> int:
        self.p.append(price)
        consec = 0
        for i in range(len(self.p)-1, -1, -1):
            if self.p[i] <= price:
                consec += 1
            else:
                break
        return consec
        
        


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)