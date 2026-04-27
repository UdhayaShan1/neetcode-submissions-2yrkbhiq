class Solution:
    def canJump(self, nums: List[int]) -> bool:
        dp = {}
        def dfs(k1):
            if k1 >= len(nums)-1:
                return True
            if k1 in dp:
                return dp[k1]
            for i in range(nums[k1]):
                if dfs(k1+i+1):
                    dp[k1] = True
                    return True
            dp[k1] = False
            return False
        return dfs(0)

