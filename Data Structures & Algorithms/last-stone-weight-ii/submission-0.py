class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        total = sum(stones)
        target = total//2

        dp = {}
        def dfs(k1, curr):
            if k1 >= len(stones):
                return abs(curr - (total-curr))

            key = (k1, curr)
            if key in dp:
                return dp[key]
            res = float('inf')
            res = min(res , dfs(k1+1, curr))

            if curr+stones[k1] <= target:
                res = min(res, dfs(k1+1, curr+stones[k1]))
            
            dp[key] = res
            return dp[key]
        return dfs(0, 0)