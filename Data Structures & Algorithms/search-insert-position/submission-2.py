class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        start = 0
        end = len(nums)-1
        res = -1
        while start <= end:
            mid = (start+end)//2
            if nums[mid] == target:
                return mid
            if nums[mid] > target:
                end = mid-1
            else:
                res = max(res, mid)
                start = mid+1
        return res+1
            