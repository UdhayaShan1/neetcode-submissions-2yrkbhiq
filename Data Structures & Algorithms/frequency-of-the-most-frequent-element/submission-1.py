class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()
        left = 0
        res = 0
        curr = 0
        for i in range(len(nums)):
            curr += nums[i]
            
            total = nums[i] * (i-left+1)
            more = total-curr

            while more > k:
                curr -= nums[left]
                left += 1
                total = nums[i] * (i-left+1)
                more = total-curr
            res = max(res, i-left+1)
        return res
            
                



            
