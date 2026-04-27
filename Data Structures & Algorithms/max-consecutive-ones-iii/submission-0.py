class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left = 0
        zeros = 0
        res = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                zeros += 1
            
            while left < len(nums) and zeros > k:
                if nums[left] == 0:
                    zeros -= 1
                left += 1
            
            res = max(res, i-left+1)
        return res