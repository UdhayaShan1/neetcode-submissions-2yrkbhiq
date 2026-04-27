class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()
        left = 0
        curr = 0
        res = 0
        for i in range(len(nums)):
            curr += nums[i]
            while True:
                cost = nums[i] * (i-left+1) - curr
                if cost > k:
                    curr -= nums[left]
                    left += 1
                else:
                    break
            res = max(res, i-left+1)
        return res


