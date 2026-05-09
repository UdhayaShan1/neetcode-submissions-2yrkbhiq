class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        p = {}
        for i in range(len(strs)):
            ref = strs[i]
            z = 0
            o = 0
            for j in ref:
                if j == '1':
                    o += 1
                else:
                    z += 1
            p[i] = [z, o]
        #print(p)
        dp = {}
        def dfs(k1, z, o):
            if z > m or o > n:
                return -float('inf')
            if k1 >= len(strs):
                return 0

            key = (k1, z, o)
            if key in dp:
                return dp[key]
            ref = p[k1]
            dp[key] = max(dfs(k1+1, z+ref[0], o+ref[1])+1, dfs(k1+1, z, o))
            return dp[key]
        return dfs(0, 0, 0)