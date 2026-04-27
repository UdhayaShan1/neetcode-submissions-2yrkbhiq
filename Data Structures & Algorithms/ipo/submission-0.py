class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        class Tmp:
            def __init__(self, profit, capital):
                self.p = profit
                self.c = capital
            def __lt__(self, o):
                return self.c < o.c
        class Tmp2:
            def __init__(self, profit, capital):
                self.p = profit
                self.c = capital
            def __lt__(self, o):
                return self.p > o.p
        ref = []
        for i in range(len(profits)):
            ref.append(Tmp(profits[i], capital[i]))
        
        ref.sort()
        start = 0
        pq = []
        import heapq

        for i in range(k):
            while start < len(ref):
                if ref[start].c <= w:
                    heapq.heappush(pq, Tmp2(ref[start].p, ref[start].c))
                    start += 1
                else:
                    break
            
            if not pq:
                break
            
            w += heapq.heappop(pq).p
        return w

            

