class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        sys.setrecursionlimit(999999)
        from functools import cache
        @cache
        def dfs(i, j):
            
            res = 1
            for k in [(0, -1), (0, 1), (1, 0), (-1, 0)]:
                new_i = i+k[0]
                new_j = j+k[1]
                if new_i < 0 or new_j < 0 or new_i >= len(matrix) or new_j >= len(matrix[0]):
                    continue
                if matrix[new_i][new_j] > matrix[i][j]:
                    res = max(res, dfs(new_i, new_j)+1)
            return res
        
        res = 0
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                res = max(res, dfs(i, j))
        return res