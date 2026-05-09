class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums = [1]+nums+[1]

        dp = {}
        def dfs(l, r):
            if l+1 == r:
                return 0
            key = (l, r)
            if key in dp:
                return dp[key]
            res = -float('inf')
            for i in range(l+1, r):
                curr = nums[l]*nums[i]*nums[r]
                res = max(res, curr+dfs(l, i)+dfs(i, r))
            dp[key] = res
            return res
        return dfs(0, len(nums)-1)
