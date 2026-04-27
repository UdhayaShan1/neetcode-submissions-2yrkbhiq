class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        res = float('inf')
        left = 0
        curr = 0
        for i in range(len(nums)):
            curr += nums[i]
            while curr >= target:
                res = min(res, i-left+1)
                curr -= nums[left]
                left += 1
        return res if res != float('inf') else 0