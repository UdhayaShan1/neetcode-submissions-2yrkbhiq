class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        from functools import cache
        @cache
        def dfs(i, j):
            if i == len(obstacleGrid)-1 and j == len(obstacleGrid[0])-1:
                return 1-obstacleGrid[i][j]
            if obstacleGrid[i][j] == 1:
                return 0
            res = 0
            if i+1 < len(obstacleGrid):
                res += dfs(i+1, j)
            if j+1 < len(obstacleGrid[0]):
                res += dfs(i, j+1)
            return res
        return dfs(0, 0)
