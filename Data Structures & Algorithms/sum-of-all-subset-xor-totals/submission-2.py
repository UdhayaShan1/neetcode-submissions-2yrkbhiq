class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        def dfs(k1, c):
            if k1 >= len(nums):
                return c
            
            return dfs(k1+1, c)+dfs(k1+1, c^nums[k1])
        return dfs(0, 0)