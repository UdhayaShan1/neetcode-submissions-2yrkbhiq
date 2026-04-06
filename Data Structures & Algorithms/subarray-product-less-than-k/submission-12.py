class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        left = 0
        curr = 1
        res = 0
        for i in range(len(nums)):
            curr = curr*nums[i]
            while left <= i and curr >= k:
                curr //= nums[left]
                left += 1
            res += max(0, i-left+1)
        return res