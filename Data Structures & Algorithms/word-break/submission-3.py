class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        chk = set(wordDict)
        from functools import cache
        @cache
        def dfs(k1):
            if k1 >= len(s):
                return True
            for i in range(1, 21):
                if k1+i >= len(s)+1:
                    break
                ref = s[k1:k1+i]
                print(ref)
                if ref in chk:
                    if dfs(k1+i):
                        return True
            return False
        return dfs(0)
