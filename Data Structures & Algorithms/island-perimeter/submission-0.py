class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        vis = {}
        def dfs(i, j):
            if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]) or grid[i][j] == 0 or (i, j) in vis:
                return 0
            vis[(i, j)] = True
            ref = 0
            for k in [(0, -1), (0, 1), (1, 0), (-1, 0)]:
                new_i = i+k[0]
                new_j = j+k[1]
                if new_i < 0 or new_j < 0 or new_i >= len(grid) or new_j >= len(grid[0]) or grid[new_i][new_j] == 0:
                    ref += 1
            return ref+dfs(i+1, j)+dfs(i-1, j)+dfs(i, j+1)+dfs(i, j-1)
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    return dfs(i, j)
            
            
                    
                
