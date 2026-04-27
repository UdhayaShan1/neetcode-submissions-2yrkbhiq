class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        for i in range(len(nums)):
            if nums[i] == val:
                nums[i] = None
        i = 0
        j = 0
        while i < len(nums):
            if nums[i] is not None:
                i += 1
                j = max(i, j)
                continue
            
            while j < len(nums) and nums[j] is None:
                j += 1
            
            if j < len(nums):
                nums[i] = nums[j]
                nums[j] = None
            i += 1
        count = 0
        for i in nums:
            if i is None:
                break
            count += 1
                
        return count