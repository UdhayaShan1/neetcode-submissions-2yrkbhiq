class Solution:
    def jump(self, nums: List[int]) -> int:
        import sys
        sys.setrecursionlimit(9999)
        dp = {}
        def dfs(k1):
            if k1 >= len(nums)-1:
                return 0
            if k1 in dp:
                return dp[k1]
            res = float('inf')
            for j in range(1, nums[k1]+1):
                res = min(res, dfs(k1+j)+1)
            dp[k1] = res
            return dp[k1]
        return dfs(0)
