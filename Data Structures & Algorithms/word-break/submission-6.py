class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        chk = set(wordDict)

        def cache(func):
            dp = {}
            def helper(*args, **kwargs):
                key = (args, tuple(sorted(kwargs.items())))
                if key in dp:
                    return dp[key]
                dp[key] = func(*args, **kwargs)
                return dp[key]
            return helper

        @cache
        def dfs(k1):
            if k1 >= len(s):
                return True
            
            res = False
            for i in range(1, 21):
                tmp = s[k1:k1+i]
                if tmp in chk:
                    res = res or dfs(k1+i)
            return res
        return dfs(0)
