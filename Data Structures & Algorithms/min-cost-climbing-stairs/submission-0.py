class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp = {}
        def dfs(k1):
            if k1 >= len(cost):
                return 0, []
            
            if k1 in dp:
                return dp[k1]
            
            res = float('inf')
            res_path = []
            first, path1 = dfs(k1+1)
            if first+cost[k1] < res:
                res = first+cost[k1]
                res_path = list(path1) + [1]
            second, path2 = dfs(k1+2)
            if second+cost[k1] < res:
                res = second+cost[k1]
                res_path = list(path2) + [2]
            dp[k1] = (res, tuple(res_path))
            return dp[k1]
        
        # print(dfs(0))
        # print(dfs(1))
        return min(dfs(0)[0], dfs(1)[0])