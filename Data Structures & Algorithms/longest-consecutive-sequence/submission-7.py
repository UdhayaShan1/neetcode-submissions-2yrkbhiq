class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        chk = {}
        for i in nums:
            chk[i] = chk.get(i, 0)+1
        dp = {}
        def dfs(no):
            if no not in chk:
                return 0
            if no in dp:
                return dp[no]
            return dfs(no+1)+1
        #print(dfs(2))
        res = 0
        for i in nums:
            res = max(res, dfs(i))
        return res
