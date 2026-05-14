class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        ref = set(dictionary)
        from functools import cache
        @cache
        def dfs(k1):
            if k1 >= len(s):
                return 0
            res = float('inf')
            for i in range(k1, len(s)):
                tmp = s[k1:i+1]
                if tmp not in ref:
                    res = min(res, dfs(i+1)+len(tmp))
                else:
                    res = min(res, dfs(i+1))
            return res
        return dfs(0)
