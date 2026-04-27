class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        def dfs(k1, curr):
            if k1 >= len(nums):
                return curr
            
            return dfs(k1+1, curr^nums[k1])+dfs(k1+1, curr)
        return dfs(0, 0)