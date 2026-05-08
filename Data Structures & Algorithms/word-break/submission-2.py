class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        chk = set(wordDict)
        dp = {}
        def dfs(k1):
            if k1 >= len(s):
                return True
            if k1 in dp:
                return dp[k1]
            
            for i in chk:
                if s.startswith(i, k1):
                    if dfs(k1+len(i)):
                        dp[k1] = True
                        return True
            dp[k1] = False
            return False

            
        return dfs(0)