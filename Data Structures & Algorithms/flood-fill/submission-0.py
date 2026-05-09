class Solution:
    def floodFill(self, grid: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        vis = {}
        def dfs(i, j, og):
            
            if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]) or (i, j) in vis or grid[i][j] != og:
                return
            vis[(i, j)] = True
            grid[i][j] = color
            dfs(i+1, j, og)
            dfs(i-1, j, og)
            dfs(i, j+1, og)
            dfs(i, j-1, og)
        dfs(sr, sc, grid[sr][sc])

        return grid

