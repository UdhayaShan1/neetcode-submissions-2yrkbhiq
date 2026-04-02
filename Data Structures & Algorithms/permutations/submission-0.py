class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        arr = [0]*len(nums)
        res = []
        def dfs(nums, arr, k1):
            if k1 >= len(nums):
                res.append(arr[:])
                return
            for i in range(len(nums)):
                if nums[i] == None:
                    continue
                og = nums[i]
                arr[k1] = og
                nums[i] = None
                dfs(nums, arr, k1+1)
                nums[i] = og
                arr[k1] = -1
        dfs(nums, arr, 0)
        return res

        