class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        from collections import deque
        q = deque()
        d = {}
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    q.append((i, j))
                    d[(i, j)] = 0
        
        while q:
            curr = q.popleft()
            for i in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                new_i = curr[0]+i[0]
                new_j = curr[1]+i[1]
                if new_i < 0 or new_j < 0 or new_i >= len(grid) or new_j >= len(grid[0]) or grid[new_i][new_j] == 0:
                    continue
                ref = (new_i, new_j)
                if ref in d:
                    continue
                d[ref] = 1+d[curr]
                q.append(ref)
        res = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    if (i, j) not in d:
                        return -1
                    res = max(res, d[(i, j)])
        return res