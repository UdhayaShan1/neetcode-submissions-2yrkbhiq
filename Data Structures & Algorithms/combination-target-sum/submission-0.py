class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        res = []
        def dfs(k1, arr):
            curr = sum(arr)
            if curr == target:
                res.append(arr[:])
                return
            if k1 >= len(nums) or curr > target:
                return
            
            dfs(k1+1, arr)
            dfs(k1, arr+[nums[k1]])
        dfs(0, [])
        return res