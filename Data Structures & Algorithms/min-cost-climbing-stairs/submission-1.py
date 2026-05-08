class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp = {}
        def dfs(k1):
            if k1 >= len(cost):
                return 0
            if k1 in dp:
                return dp[k1]
            dp[k1] = min(dfs(k1+1)+cost[k1], dfs(k1+2)+cost[k1])
            return dp[k1]
        return min(dfs(0), dfs(1))