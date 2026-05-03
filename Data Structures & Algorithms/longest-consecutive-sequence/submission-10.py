class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        dp = {}
        def dfs(no):
            if no not in s:
                return 0
            if no in dp:
                return dp[no]
            dp[no] = dfs(no+1)+1
            return dp[no]
        res = 0
        for i in nums:
            res = max(res, dfs(i))
        return res

