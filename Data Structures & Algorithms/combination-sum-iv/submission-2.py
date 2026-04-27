class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        dp = {}
        def dfs(n):
            if n == 0:
                return 1
            if n in dp:
                return dp[n]
            res = 0
            for i in nums:
                if n-i >= 0:
                    res += dfs(n-i)
            dp[n] = res
            return res
        return dfs(target)
