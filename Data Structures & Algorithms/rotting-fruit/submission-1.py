class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = deque()

        dist = {}
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    q.append((i,j))
                    dist[(i,j)] = 0
        
        #print(q)

        while q:
            curr = q.popleft()

            for i in [(0, -1), (0, 1), (1, 0), (-1, 0)]:
                new_i = curr[0]+i[0]
                new_j = curr[1]+i[1]
                if new_i < 0 or new_j < 0 or new_i >= len(grid) or new_j >= len(grid[0]) or grid[new_i][new_j] == 0 :
                    continue
                nw = (new_i, new_j)
                if nw not in dist:
                    dist[nw] = float('inf')
                if 1+dist[curr] < dist[nw]:
                    dist[nw] = 1+dist[curr]
                    q.append(nw)
        #print(dist)

        res = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0:
                    continue
                if (i,j) not in dist:
                    return -1
                res = max(res, dist[(i,j)])
        return res
