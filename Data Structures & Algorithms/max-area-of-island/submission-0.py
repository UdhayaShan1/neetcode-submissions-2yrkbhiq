class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        chk = {}
        def dfs(i, j):
            chk[(i, j)] = 1
            y1 = 1
            for k in [(0, -1), (0, 1), (1, 0), (-1, 0)]:
                new_i = i+k[0]
                new_j = j+k[1]
                if new_i < 0 or new_j < 0 or new_i >= len(grid) or new_j >= len(grid[0]) or (new_i, new_j) in chk or grid[new_i][new_j] == 0:
                    continue
                y1 += dfs(new_i, new_j)
            return y1
        res = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0 or (i,j) in chk:
                    continue
                res = max(res, dfs(i, j))
        return res

        