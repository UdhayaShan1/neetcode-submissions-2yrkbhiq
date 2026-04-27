class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        left = 0
        nums.sort()
        curr = 0
        res = 0
        for i in range(len(nums)):
            curr += nums[i]
            more = nums[i]*(i-left+1)-curr
            while more > k:
                curr -= nums[left]
                left += 1
                more = nums[i]*(i-left+1)-curr
                
            res = max(res, i-left+1)
        return res
            
