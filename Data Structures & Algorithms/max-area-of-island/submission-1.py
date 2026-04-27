class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        vis = {}
        def dfs(i, j):
            
            res = 1
            vis[(i,j)] = True
            for k in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
                new_i = i+k[0]
                new_j = j+k[1]
                ref = (new_i, new_j)
                if ref in vis:
                    continue
                if new_i < 0 or new_j < 0 or new_i >= len(grid) or new_j >= len(grid[0]) or grid[new_i][new_j] == 0:
                    continue
                res += dfs(new_i, new_j)
            return res
        
        res = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if (i,j) in vis or grid[i][j] == 0:
                    continue
                res = max(res, dfs(i, j))
        return res
                