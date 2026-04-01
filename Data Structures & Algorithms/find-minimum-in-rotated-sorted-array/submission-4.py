class Solution:
    def findMin(self, nums: List[int]) -> int:
        s = 0
        e = len(nums)-1
        res = float('inf')
        while s <= e:
            mid = (s+e)//2
            if nums[s] <= nums[mid]:
                res = min(res, nums[s])
                s = mid+1
            else:
                res = min(res, nums[mid])
                e = mid-1
        return res

