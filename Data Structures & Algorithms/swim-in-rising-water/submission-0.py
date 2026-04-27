class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        import heapq
        dist = {}
        pq = []
        class Node:
            def __init__(self, val, dist):
                self.val = val
                self.dist = dist
            def __lt__(self, o):
                return self.dist < o.dist
        
        heapq.heappush(pq, Node((0,0), grid[0][0]))
        dist[(0,0)] = grid[0][0]
        while len(pq) > 0:
            curr = heapq.heappop(pq)
            for i in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
                new_i = curr.val[0] + i[0]
                new_j = curr.val[1] + i[1]
                if new_i < 0 or new_j < 0 or new_i >= len(grid) or new_j >= len(grid[0]):
                    continue
                chk = max(grid[curr.val[0]][curr.val[1]], grid[new_i][new_j], dist[(curr.val[0], curr.val[1])])
                if (new_i, new_j) not in dist:
                    dist[(new_i, new_j)] = float('inf')
                if chk < dist[(new_i, new_j)]:
                    dist[(new_i, new_j)] = chk
                    heapq.heappush(pq, Node((new_i, new_j), chk))
        #print(dist)
        return dist[(len(grid)-1, len(grid[0])-1)]
