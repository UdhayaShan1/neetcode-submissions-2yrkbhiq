class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        nums = [-float('inf')] + nums + [-float('inf')]
        start = 1
        end = len(nums)-2
        while start <= end:
            mid = (start+end)//2
            if nums[mid] > nums[mid-1] and nums[mid] > nums[mid+1]:
                return mid-1
            if nums[mid] >= nums[mid-1] and nums[mid] <= nums[mid+1]:
                start = mid+1
            else:
                end = mid-1
        
