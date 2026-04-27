class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        chk = {}
        for i in wordDict:
            chk[i] = True
        
        res = []
        def dfs(k1, arr):
            if k1 >= len(s):
                res.append(arr[:])
                return
            
            for i in range(k1, len(s)):
                tmp = s[k1:i+1]
                if tmp not in chk:
                    continue
                #print(tmp)
                dfs(i+1, arr+[tmp])
        dfs(0, [])
        #print(res)
        res2 = []
        for i in res:
            res2.append(' '.join(i))
        return res2