class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adjList = {}
        for i in range(1, n+1):
            adjList[i] = []
        for i in times:
            adjList[i[0]].append((i[1], i[2]))
        
        class Tmp:
            def __init__(self, n, d):
                self.n = n
                self.d = d
            def __lt__(self, o):
                return self.d < o.d
        
        pq = []
        d = {}
        d[k] = 0
        heapq.heappush(pq, Tmp(k, 0))
        while pq:
            curr = heapq.heappop(pq)
            if curr.d > d[curr.n]:
                continue
            for i in adjList[curr.n]:
                if i[1]+curr.d < d.get(i[0], float('inf')):
                    d[i[0]] = i[1]+curr.d
                    heapq.heappush(pq, Tmp(i[0], d[i[0]]))
        #print(d)
        return -1 if len(d) != n else max(d.values())
        #return 1