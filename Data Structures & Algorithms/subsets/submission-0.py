class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        def dfs(k1, arr):
            if k1 >= len(nums):
                res.append(arr[:])
                return
            
            dfs(k1+1, arr)
            dfs(k1+1, arr+[nums[k1]])
        dfs(0, [])
        return res