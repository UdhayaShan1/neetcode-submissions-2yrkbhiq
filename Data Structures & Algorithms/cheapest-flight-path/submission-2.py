class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        import heapq
        dist = {}
        pq = []
        adjList = {}
        for i in range(n):
            adjList[i] = []
        for i in flights:
            adjList[i[0]].append((i[1], i[2]))
        class Tmp:
            def __init__(self, v, d, k):
                self.v = v
                self.d = d
                self.k = k
            def __lt__(self, o):
                return self.d < o.d
        heapq.heappush(pq, Tmp(src, 0, k+1))
        dist[(src, k+1)] = 0
        while len(pq) > 0:
            curr = heapq.heappop(pq)
            if curr.k == 0:
                continue
            for i in adjList[curr.v]:
                if (i[0], curr.k-1) not in dist:
                    dist[(i[0], curr.k-1)] = float('inf')
                if i[-1] + curr.d < dist[(i[0], curr.k-1)]:
                    dist[(i[0], curr.k-1)] = i[-1] + curr.d
                heapq.heappush(pq, Tmp(i[0], dist[(i[0], curr.k-1)], curr.k-1))
        res = float('inf')
        for i in dist:
            if i[0] == dst:
                res = min(res, dist[i])
        return res if res != float('inf') else -1

