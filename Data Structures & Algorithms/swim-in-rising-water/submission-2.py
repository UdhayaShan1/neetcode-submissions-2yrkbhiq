class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        pq = []
        d = {}
        class Tmp:
            def __init__(self, pos, d):
                self.pos = pos
                self.d = d
            def __lt__(self, o):
                return self.d < o.d
        
        heapq.heappush(pq, Tmp((0, 0), 0))
        d[(0, 0)] = grid[0][0]

        while pq:
            curr = heapq.heappop(pq)
            if curr.d > d[curr.pos]:
                continue
            curr_i = curr.pos[0]
            curr_j = curr.pos[1]
            for i in [(0, -1), (0, 1), (1, 0), (-1, 0)]:
                new_i = curr_i + i[0]
                new_j = curr_j + i[1]
                if new_i < 0 or new_j < 0 or new_i >= len(grid) or new_j >= len(grid[0]):
                    continue
                new_d = max(d[curr.pos], grid[new_i][new_j])
                ref = (new_i, new_j)
                if new_d < d.get(ref, float('inf')):
                    d[ref] = new_d
                    heapq.heappush(pq, Tmp(ref, d[ref]))
        #print(d)
        return d[(len(grid)-1, len(grid[0])-1)]
