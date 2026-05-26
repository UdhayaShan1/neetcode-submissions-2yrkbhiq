class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        vis = {}
        def dfs(i, j):
            if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]) or grid[i][j] == 0:
                return 0
            res = 1
            vis[(i, j)] = True
            for k in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                new_i = i+k[0]
                new_j = j+k[1]
                if (new_i, new_j) in vis:
                    continue
                res += dfs(new_i, new_j)
            return res
        res = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0 or (i, j) in vis:
                    continue
                res = max(res, dfs(i, j))
        return res
        