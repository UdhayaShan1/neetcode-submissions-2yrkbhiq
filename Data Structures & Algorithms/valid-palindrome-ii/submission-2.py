class Solution:
    def validPalindrome(self, s: str) -> bool:
        dp = {}
        def dfs(i, j, deleted):
            if i >= j:
                return True
            key = (i, j, deleted)
            if key in dp:
                return dp[key]
            if s[i] == s[j]:
                dp[key] = dfs(i+1,j-1, deleted)
            else:
                if deleted:
                    dp[key] = False
                else:
                    dp[key] = dfs(i+1, j, True) or dfs(i, j-1, True)
            return dp[key]
        return dfs(0, len(s)-1, False)