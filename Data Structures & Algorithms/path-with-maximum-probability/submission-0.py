class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:
        class Tmp:
            def __init__(self, n, d):
                self.n = n
                self.d = d
            def __lt__(self, o):
                return self.d < o.d
        
        adjList = {}
        for i in range(n):
            adjList[i] = []
        for i in range(len(edges)):
            ref = edges[i]
            adjList[ref[0]].append((ref[1], succProb[i]))
            adjList[ref[1]].append((ref[0], succProb[i]))
        
        import heapq
        d = {}
        d[start] = 1
        pq = []
        heapq.heappush(pq, Tmp(start, 1))

        while pq:
            curr = heapq.heappop(pq)
            for i in adjList[curr.n]:
                new_p = curr.d * i[-1]
                if new_p > d.get(i[0], -float('inf')):
                    d[i[0]] = new_p
                    heapq.heappush(pq, Tmp(i[0], d[i[0]]))
        if end not in d:
            return 0
        return d[end]