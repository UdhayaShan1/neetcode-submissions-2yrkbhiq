class Solution:
    def findMin(self, nums: List[int]) -> int:
        start = 0
        end = len(nums)-1
        res = float('inf')
        while start <= end:
            mid = (start+end)//2
            res = min(res, nums[mid])
            if nums[start] > nums[end]:
                if nums[mid] >= nums[start]:
                    start = mid+1
                else:
                    end = mid-1
            else:
                end = mid-1

        return res
