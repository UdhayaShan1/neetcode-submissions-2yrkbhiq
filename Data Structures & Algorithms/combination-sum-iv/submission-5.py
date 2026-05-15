class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        from functools import cache
        @cache
        def dfs(no):
            if no == target:
                return 1
            if no > target:
                return 0
            res = 0
            for i in nums:
                res += dfs(no+i)
            return res
        return dfs(0)