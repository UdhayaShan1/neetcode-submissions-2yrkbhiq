class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        zero = 0
        left = 0
        res = -float('inf')
        for i in range(len(nums)):
            if nums[i] == 0:
                zero += 1
            while zero > k:
                if nums[left] == 0:
                    zero -= 1
                left += 1
            res = max(res, i-left+1)
        return res