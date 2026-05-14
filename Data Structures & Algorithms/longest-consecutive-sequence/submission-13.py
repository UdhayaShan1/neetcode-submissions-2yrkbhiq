class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        dp = {}
        def dfs(n):
            if n not in s:
                return 0
            if n in dp:
                return dp[n]
            dp[n] = dfs(n+1)+1
            return dp[n]
        res = 0
        for i in nums:
            res = max(res, dfs(i))
        return res
        
