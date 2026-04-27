class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        dp = {}
        def dfs(i, j):
            if (i,j) in dp:
                return dp[(i,j)]
            res = 0
            for k in [(0,-1), (0,1), (-1, 0), (1, 0)]:
                new_i = i+k[0]
                new_j = j+k[1]
                if new_i < 0 or new_j < 0 or new_i >= len(matrix) or new_j >= len(matrix[0]) or matrix[new_i][new_j] <= matrix[i][j]:
                    continue
                res = max(res, dfs(new_i, new_j)+1)
            dp[(i,j)] = res
            return res
        res = -float('inf')
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                res = max(res, dfs(i, j))
        return res+1
                
                
                