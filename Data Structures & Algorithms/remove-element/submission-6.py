class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        for i in range(len(nums)):
            if nums[i] == val:
                nums[i] = None
        
        i = 0
        while i < len(nums):
            if nums[i] is not None:
                i += 1
                continue
            find = i
            while find < len(nums) and nums[find] is None:
                find += 1
            #print(i, find, nums[i])
            if find < len(nums):
                nums[i], nums[find] = nums[find], nums[i]
            i += 1
        #print(nums)
        count = 0
        for i in nums:
            if i is None:
                break
            count += 1
        return count