class Solution:
    def numDecodings(self, s: str) -> int:
        dp = {}
        def dfs(k1):
            if k1 >= len(s):
                return 1
            if s[k1] == '0':
                return 0
            if k1 in dp:
                return dp[k1]
            res = dfs(k1+1)
            tmp = s[k1:k1+2]
            if len(tmp) == 2 and int(tmp) <= 26:
                res += dfs(k1+2)
            dp[k1] = res
            return dp[k1]
        return dfs(0)