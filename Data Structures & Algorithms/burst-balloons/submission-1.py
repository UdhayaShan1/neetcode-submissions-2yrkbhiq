class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        from functools import cache
        nums = [1]+nums+[1]
        @cache
        def dfs(l, r):
            if l+1 == r:
                return 0
            
            res = -float('inf')
            for i in range(l+1, r):
                curr = dfs(l, i) + nums[l]*nums[i]*nums[r] + dfs(i, r)
                res = max(res, curr)
            return res
        return dfs(0, len(nums)-1)

