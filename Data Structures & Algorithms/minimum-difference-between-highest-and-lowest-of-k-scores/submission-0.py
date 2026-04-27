class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        nums.sort()
        res = float('inf')
        for i in range(len(nums)):
            if i+k-1 < len(nums):
             res = min(res, nums[i+k-1]-nums[i])
        return res