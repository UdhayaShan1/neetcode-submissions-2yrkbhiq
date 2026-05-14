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
        import heapq
        d[k] = 0
        heapq.heappush(pq, Tmp(k, 0))
        while pq:
            curr = heapq.heappop(pq)
            if curr.d > d[curr.n]:
                continue
            for i in adjList.get(curr.n, []):
                new_d = d[curr.n]+i[1]
                if new_d < d.get(i[0], float('inf')):
                    d[i[0]] = new_d
                    heapq.heappush(pq, Tmp(i[0], d[i[0]]))
        #print(d)
        for i in range(1, n+1):
            if i not in d:
                return -1
        return max(d.values())