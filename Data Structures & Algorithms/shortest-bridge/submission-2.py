class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        vis = {}
        def dfs(i, j, c):
            if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]) or (i, j) in vis or grid[i][j] == 0:
                return
            vis[(i, j)] = c
            dfs(i+1, j, c)
            dfs(i-1, j, c)
            dfs(i, j-1, c)
            dfs(i, j+1, c)
        c = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if (i, j) in vis or grid[i][j] != 1:
                    continue
                c += 1
                dfs(i, j, c)
        print(vis)

        q = deque()
        d = {}
        for i in range(len(grid)):
            for j in range(len(grid)):
                if vis.get((i, j), -1) == 1:
                    q.append((i, j))
                    d[(i, j)] = 0
        
        while q:
            curr = q.popleft()
            for k in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                new_i = curr[0]+k[0]
                new_j = curr[1]+k[1]
                if new_i < 0 or new_j < 0 or new_i >= len(grid) or new_j >= len(grid[0]) or (new_i, new_j) in d:
                    continue
                d[(new_i, new_j)] = 1+d[curr]
                q.append((new_i, new_j))
        #print(d)

        res = float('inf')
        for i in d:
            if vis.get(i, -1) == 2:
                res = min(res, d[i])
        return res-1

                
                
            