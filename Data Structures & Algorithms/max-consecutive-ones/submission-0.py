class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        i = 0
        res = 0
        while i < len(nums):
            if nums[i] != 1:
                i += 1
                continue
            curr = 0
            while i < len(nums) and nums[i] == 1:
                i += 1
                curr += 1
            res = max(res, curr)
        return res
        