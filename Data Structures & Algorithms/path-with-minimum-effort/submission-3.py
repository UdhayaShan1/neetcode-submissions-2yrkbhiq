class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        class Tmp:
            def __init__(self, coor, d):
                self.coor = coor
                self.d = d
            def __lt__(self, o):
                return self.d < o.d
        
        pq = []
        d = {}
        d[(0, 0)] = 0
        heapq.heappush(pq, Tmp((0, 0), 0))
        while pq:
            curr = heapq.heappop(pq)
            if curr.d > d[curr.coor]:
                continue
            for k in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                new_i = curr.coor[0]+k[0]
                new_j = curr.coor[1]+k[1]
                if new_i < 0 or new_j < 0 or new_i >= len(heights) or new_j >= len(heights[0]):
                    continue
                new_d = max(curr.d, abs(heights[curr.coor[0]][curr.coor[1]] - heights[new_i][new_j]))
                ref = (new_i, new_j)
                if new_d < d.get(ref, float('inf')):
                    d[ref] = new_d
                    heapq.heappush(pq, Tmp(ref, d[ref]))
        #print(d)
        return d[(len(heights)-1, len(heights[0])-1)]