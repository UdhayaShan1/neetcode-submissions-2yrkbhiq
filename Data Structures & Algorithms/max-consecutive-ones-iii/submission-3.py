class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        ones = 0
        zeros = 0
        left = 0
        res = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                ones += 1
            else:
                zeros += 1
            
            while zeros > k:
                if nums[left] == 1:
                    ones -= 1
                else:
                    zeros -= 1
                left += 1
            res = max(res, i-left+1)
        return res