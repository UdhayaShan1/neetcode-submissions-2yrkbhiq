class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        def at_most(k):
            left = 0
            curr = 0
            res = 0
            for i in range(len(nums)):
                curr += nums[i]
                while left < len(nums) and curr > k:
                    curr -= nums[left]
                    left += 1
                
                res += max(0, i-left+1)
            return res
        
        return at_most(goal)-at_most(goal-1)
                
