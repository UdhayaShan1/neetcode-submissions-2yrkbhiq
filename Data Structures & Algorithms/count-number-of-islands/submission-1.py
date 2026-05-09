class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        vis = {}
        def dfs(i, j):
            if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]) or (i, j) in vis or grid[i][j] == '0':
                return
            vis[(i,j)] = True
            dfs(i+1, j)
            dfs(i-1, j)
            dfs(i, j-1)
            dfs(i, j+1)
        res = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if (i, j) in vis or grid[i][j] == '0':
                    continue
                dfs(i, j)
                res += 1
        return res
