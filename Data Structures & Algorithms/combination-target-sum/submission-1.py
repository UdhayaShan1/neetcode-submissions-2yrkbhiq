class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        def dfs(k1, arr, t):
            if t == target:
                res.append(arr[:])
                return
            if k1 >= len(nums) or t > target:
                return
            
            dfs(k1, arr+[nums[k1]], t+nums[k1])
            dfs(k1+1, arr, t)
        dfs(0, [], 0) 
        return res