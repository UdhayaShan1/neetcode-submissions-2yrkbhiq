class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        def canSplit(threshold):
            curr = 0
            total = 1
            i = 0
            while i < len(nums):
                if curr + nums[i] <= threshold:
                    curr += nums[i]
                    i += 1
                else:
                    total += 1
                    curr = nums[i]
                    i += 1
            return total <= k
        

        start = max(nums)
        end = sum(nums)
        res = float('inf')
        while start <= end:
            mid = (start+end)//2
            if canSplit(mid):
                res = mid
                end = mid-1
            else:
                start = mid+1
        return res
