class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        ref = []
        for i in range(len(nums)):
            s = 0
            e = len(ref)-1
            res = -1
            while s <= e:
                mid = (s+e)//2
                if ref[mid] < nums[i]:
                    s = mid+1
                else:
                    res = mid
                    e = mid-1
            if res == -1:
                ref.append(nums[i])
            else:
                ref[res] = nums[i]
        return len(ref)