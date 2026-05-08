class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        chk = set(words)
        def dfs(k1, ref, dp):
            if k1 >= len(ref):
                return True
            if k1 in dp:
                return dp[k1]
            for i in range(k1, len(ref)):
                tmp = ref[k1:i+1]
                if tmp in chk and tmp != ref:
                    if dfs(i+1, ref, dp):
                        dp[k1] = True
                        return True
            dp[k1] = False
            return False
        #print(dfs(0, 'hippopotamuses', dp))


        res = []
        for i in words:
            if dfs(0, i, {}):
                res.append(i)
        return res

