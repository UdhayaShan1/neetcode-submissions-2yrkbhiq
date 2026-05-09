class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        vis = {}
        def dfs(i, j):
            if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]) or (i, j) in vis or grid[i][j] == 0:
                return 0
            vis[(i,j)] = True
            return 1+dfs(i+1, j)+dfs(i-1, j)+dfs(i, j-1)+dfs(i, j+1)
        res = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                res = max(res, dfs(i, j))
        return res