class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = {}
        def dfs(k1, startBought, prevBought):
            if k1 >= len(nums):
                return 0
            key = (k1, startBought, prevBought)
            if key in dp:
                return dp[key]
            if k1 == 0:
                dp[key] = max(dfs(k1+1, True, True)+nums[k1], dfs(k1+1, False, False))
            else:
                res = -float('inf')
                if (k1 == len(nums)-1 and startBought) or prevBought:
                    res = max(res, dfs(k1+1, startBought, False))
                else:
                    res = max(res, dfs(k1+1, startBought, False), dfs(k1+1, startBought, True)+nums[k1])
                dp[key] = res
            return dp[key]
        return dfs(0, False, False)