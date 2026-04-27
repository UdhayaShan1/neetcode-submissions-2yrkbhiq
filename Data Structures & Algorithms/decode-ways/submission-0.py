class Solution:
    def numDecodings(self, s: str) -> int:
        ref = "abcdefghijklmnopqrstuvwxyz"
        dp = {}
        def dfs(k1):
            if k1 >= len(s):
                return 1
            if k1 in dp:
                return dp[k1]
            res = 0
            for i in range(k1, len(s)):
                ref = s[k1:i+1]
                if ref and (int(ref) > 26 or ref[0] == '0'):
                    break
                res += dfs(i+1)
            dp[k1] = res
            return dp[k1]
        return dfs(0)
                
                