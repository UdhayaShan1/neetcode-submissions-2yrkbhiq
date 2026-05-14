class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0
        curr = 0
        res = float('inf')
        for i in range(len(nums)):
            curr += nums[i]
            while curr >= target:
                res = min(res, i-left+1)
                curr -= nums[left]
                left += 1
        return res if res != float('inf') else 0