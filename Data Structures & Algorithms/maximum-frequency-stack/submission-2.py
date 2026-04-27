import heapq

class Tmp:
    def __init__(self, val, pos, freq):
        self.val = val
        self.pos = pos
        self.freq = freq
    def __lt__(self, o):
        if self.freq != o.freq:
            return self.freq > o.freq
        return self.pos > o.pos

class FreqStack:

    def __init__(self):
        self.pq = []
        self.chk = {}
        self.pos = 0

    def push(self, val: int) -> None:
        self.chk[val] = self.chk.get(val, 0)+1
        print(val, self.chk)
        heapq.heappush(self.pq, Tmp(val, self.pos, self.chk[val]))
        self.pos += 1
        

    def pop(self) -> int:
        top = heapq.heappop(self.pq)
        self.chk[top.val] -= 1
        return top.val

        
        


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()