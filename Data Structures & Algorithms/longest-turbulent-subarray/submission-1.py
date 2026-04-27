class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        dp = {}
        def dfs(k1, prev, higher):
            if k1 >= len(arr):
                return 0
            if higher and arr[k1] <= prev:
                return 0
            if not higher and arr[k1] >= prev:
                return 0
            key = (k1, prev, higher)
            if key in dp:
                return dp[key]
            
            dp[key] = max(dfs(k1+1, arr[k1], not higher)+1, dfs(k1+1, arr[k1], not higher)+1)

            return dp[key]
        res = 0
        for i in range(len(arr)):
            res = max(res, dfs(i, float('inf'), False))
            res = max(res, dfs(i, -float('inf'), True))
        return res