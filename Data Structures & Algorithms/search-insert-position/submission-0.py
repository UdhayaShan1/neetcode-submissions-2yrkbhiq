class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        pos = -1
        start = 0
        end = len(nums)-1
        while start <= end:
            mid = (start+end)//2
            if nums[mid] < target:
                pos = max(pos, mid)
                start = mid+1
            else:
                end = mid-1
        return pos+1
