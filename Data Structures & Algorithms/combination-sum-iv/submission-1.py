class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        dp = {}
        def dfs(target):
            if target == 0:
                return 1
            if target < 0:
                return 0
            if target in dp:
                return dp[target]
            res = 0
            for i in nums:
                res += dfs(target-i)
            dp[target] = res
            return res

        return dfs( target)

