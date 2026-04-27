class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        for i in range(len(nums)):
            if nums[i] == val:
                nums[i] = None
        print(nums)
        i = 0
        j = i+1
        while i < len(nums):
            if nums[i] is not None:
                i += 1
                j = max(j, i+1)
                continue
            
            while j < len(nums) and nums[j] is None:
                j += 1
            if i >= len(nums) or j >= len(nums):
                break
            nums[i] = nums[j]
            nums[j] = None
            i += 1
            j += 1
        #print(nums)
        l = 0
        for i in nums:
            if i is None:
                break
            l += 1
        return l