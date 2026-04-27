class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        chk = {}
        for i in wordDict:
            chk[i] = True
        

        res = []
        def dfs(k1, arr):
            if k1 >= len(s):
                res.append(' '.join(arr))
                return
            
            for i in range(k1, len(s)):
                tmp = s[k1:i+1]
                if tmp not in chk:
                    continue
                dfs(i+1, arr+[tmp])
        dfs(0, [])
        return res