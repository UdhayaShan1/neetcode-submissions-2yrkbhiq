class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []
        d = {}
        def dfs(nums, arr):
            if not nums:
                ref = tuple(arr)
                if ref in d:
                    return
                d[ref] = True
                res.append(arr[:])
                return
            for i in range(len(nums)):
                dfs(nums[:i]+nums[i+1:], arr+[nums[i]])
        dfs(nums, [])
        return res
        