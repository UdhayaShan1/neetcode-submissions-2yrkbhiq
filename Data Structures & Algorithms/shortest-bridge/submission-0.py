class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        vis = {}
        def dfs(i, j, mark):
            vis[(i,j)] = True
            grid[i][j] = mark
            for k in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
                new_i = i+k[0]
                new_j = j+k[1]
                if new_i < 0 or new_j < 0 or new_i >= len(grid) or new_j >= len(grid[0]) or (new_i, new_j) in vis or grid[new_i][new_j] == 0:
                    continue
                dfs(new_i, new_j, mark)
        stop = False
        for i in range(len(grid)):
            if stop:
                break
            for j in range(len(grid[0])):
                if grid[i][j]:
                    dfs(i, j, 2)
                    stop = True
                    break
        from collections import deque
        q = deque()
        d = {}
        water = {}
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    q.append((i,j))
                    d[(i,j)] = 0
                if grid[i][j] == 0:
                    water[(i,j)] = True

        #print(grid)

        while q:
            curr = q.popleft()
            for k in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
                new_i = curr[0]+k[0]
                new_j = curr[1]+k[1]
                if new_i < 0 or new_j < 0 or new_i >= len(grid) or new_j >= len(grid[0]):
                    continue
                ref = (new_i, new_j)
                if ref not in d:
                    d[ref] = float('inf')
                if 1+d[curr] < d[ref]:
                    d[ref] = 1+d[curr]
                    q.append(ref)
        #print(d)
        res = float('inf')
        for i in d:
            if d[i] == 0 or i in water:
                continue
            res = min(res, d[i]-1)
        return res
                    
                
