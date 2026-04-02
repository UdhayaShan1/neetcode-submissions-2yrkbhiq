class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        d = {}
        for i in wordDict:
            d[i] = True
        res = []
        def dfs(k1, arr):
            if k1 >= len(s):
                res.append(' '.join(arr[:]))
                return

            for i in range(k1, len(s)):
                ref = s[k1:i+1]
                if ref in d:
                    arr.append(ref)
                    dfs(i+1, arr)
                    arr.pop()
        dfs(0, [])
        return res
                    