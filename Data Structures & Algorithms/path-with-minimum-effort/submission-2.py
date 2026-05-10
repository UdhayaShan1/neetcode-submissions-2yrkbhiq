class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        q = deque()
        pq = []
        d= {}
        import heapq
        class Tmp:
            def __init__(self, coor, d):
                self.coor = coor
                self.d = d
            def __lt__(self, o):
                return self.d < o.d
        
        heapq.heappush(pq, Tmp((0, 0), 0))
        d[(0, 0)] = 0
        while pq:
            curr = heapq.heappop(pq)
            coor = curr.coor
            for k in [(0, -1), (0, 1), (1, 0), (-1, 0)]:
                new_i = coor[0]+k[0]
                new_j = coor[1]+k[1]
                if new_i < 0 or new_j < 0 or new_i >= len(heights) or new_j >= len(heights[0]):
                    continue
                new_d = max(d[coor], abs(heights[new_i][new_j] - heights[coor[0]][coor[1]]))
                if new_d < d.get((new_i, new_j), float('inf')):
                    d[(new_i, new_j)] = new_d
                    heapq.heappush(pq, Tmp((new_i, new_j), new_d))
        print(d)
        return d[(len(heights)-1, len(heights[0])-1)]
