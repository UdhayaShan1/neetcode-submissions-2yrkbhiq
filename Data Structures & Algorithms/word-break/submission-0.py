class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        d = set(wordDict)
        dp = {}
        def dfs(k1):
            if k1 >= len(s):
                return True
            if k1 in dp:
                return dp[k1]
            for i in range(k1, len(s)):
                tmp = s[k1:i+1]
                if tmp in d:
                    if dfs(i+1):
                        dp[k1] = True
                        return True
            dp[k1] = False
            return False
        return dfs(0)
