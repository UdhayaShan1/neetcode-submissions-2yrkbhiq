class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        min1 = 1
        max1 = 1
        res = nums[0]
        for i in range(len(nums)):
            tmp = min1
            min1 = min(nums[i], nums[i] * max1, nums[i] * min1)
            max1 = max(nums[i], nums[i] * max1, nums[i] * tmp)
            res = max(res, max1)
        return res
        