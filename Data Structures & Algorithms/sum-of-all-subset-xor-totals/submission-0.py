class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        def dfs(k1, curr):
            if k1 >= len(nums):
                return curr
            
            incl = dfs(k1+1, curr^nums[k1])
            excl = dfs(k1+1, curr)
            return incl+excl
        return dfs(0, 0)