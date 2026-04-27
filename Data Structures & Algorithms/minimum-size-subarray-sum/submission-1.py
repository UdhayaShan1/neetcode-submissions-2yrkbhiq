class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        curr = 0
        left = 0
        res = float('inf')
        for i in range(len(nums)):
            curr += nums[i]

            if curr < target:
                continue
            
            while curr >= target:
                res = min(res, i-left+1)
                curr -= nums[left]
                left += 1
            
        return res if res != float('inf') else 0