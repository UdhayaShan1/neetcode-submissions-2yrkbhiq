class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        class Tmp:
            def __init__(self, p, s):
                self.p = p
                self.s = s
            def __lt__(self, o):
                return self.p < o.p
        ref = []
        for i in range(len(position)):
            ref.append(Tmp(position[i], speed[i]))
        ref.sort()
        s = []
        for i in ref:
            nxt = (target-i.p)/i.s
            while len(s) > 0 and nxt >= s[-1]:
                s.pop()
            s.append(nxt)
        return len(s)
