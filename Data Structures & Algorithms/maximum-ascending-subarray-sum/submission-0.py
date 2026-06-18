class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        res = 0
        curr = 0
        i = 0
        while i < len(nums):
            curr = nums[i]
            res = max(res, curr)
            i += 1
            while i < len(nums) and nums[i] > nums[i-1]:
                curr += nums[i]
                i += 1
            res = max(res, curr)
        return res
        