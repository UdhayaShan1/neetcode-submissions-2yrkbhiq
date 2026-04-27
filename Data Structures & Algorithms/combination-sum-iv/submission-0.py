class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        nums.sort()
        dp = {}
        def dfs(curr):
            if curr == target:
                return 1
            if curr > target:
                return 0
            if curr in dp:
                return dp[curr]
            y1 = 0
            for i in nums:
                y1 += dfs(curr+i)
            dp[curr] = y1
            return dp[curr]

        return dfs(0)