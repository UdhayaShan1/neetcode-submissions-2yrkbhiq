class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        class Tmp:
            def __init__(self, coor, d):
                self.coor = coor
                self.d = d
            def __lt__(self, o):
                return self.d < o.d
        ref = (0, 0)
        d = {}
        pq = []
        d[ref] = grid[0][0]
        heapq.heappush(pq, Tmp(ref, d[ref]))
        while pq:
            curr = heapq.heappop(pq)
            for k in [(0, 1), (0, -1), (-1, 0), (1, 0)]:
                new_i = curr.coor[0]+k[0]
                new_j = curr.coor[1]+k[1]
               
                if new_i < 0 or new_j < 0 or new_i >= len(grid) or new_j >= len(grid[0]):
                    continue
                new_d = max(d[curr.coor], grid[new_i][new_j])
                ref = (new_i, new_j)
                #print('@', ref)
                if new_d < d.get(ref, float('inf')):
                    d[ref] = new_d
                    heapq.heappush(pq, Tmp(ref, d[ref]))
        #print(d)
        return d[(len(grid)-1, len(grid[0])-1)]
