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
            res = 0
            res += dfs(k1+1)
            ref2 = s[k1:k1+2]
            #print(k1, ref2)
            if len(ref2) == 2 and int(ref2) <= 26:
                res += dfs(k1+2)
            dp[k1] = res
            return res
        return dfs(0)