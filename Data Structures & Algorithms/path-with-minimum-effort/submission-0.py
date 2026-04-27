class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        class Tmp:
            def __init__(self, coor, d):
                self.coor = coor
                self.d = d
            def __lt__(self, o):
                return self.d < o.d

        import heapq
        pq = []
        dist = {}
        heapq.heappush(pq, Tmp((0, 0), 0))
        dist[(0, 0)] = 0

        while len(pq) > 0:
            curr = heapq.heappop(pq)
            coor = curr.coor
            d = curr.d
            if coor == (len(heights)-1, len(heights[0])-1):
                return d

            for i in [(0, -1), (0, 1), (1, 0), (-1, 0)]:
                new_i = coor[0]+i[0]
                new_j = coor[1]+i[1]
                if new_i < 0 or new_j < 0 or new_i >= len(heights) or new_j >= len(heights[0]):
                    continue

                new_d = max(dist[coor], abs(heights[new_i][new_j] - heights[coor[0]][coor[1]]))
                ref = (new_i, new_j)
                if ref not in dist:
                    dist[ref] = float('inf')
                if new_d < dist[ref]:
                    dist[ref] = new_d
                    heapq.heappush(pq, Tmp(ref, new_d))
        