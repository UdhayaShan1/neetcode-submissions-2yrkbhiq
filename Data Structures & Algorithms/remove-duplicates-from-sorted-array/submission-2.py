class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        chk = {}
        for i in range(len(nums)):
            if nums[i] in chk:
                nums[i] = None
            else:
                chk[nums[i]] = True
        #print(nums)
        i = 0
        j = 0
        while i < len(nums):
            if nums[i] is not None:
                i += 1
                j = max(j, i)
                continue
            while j < len(nums) and nums[j] is None:
                j += 1
            if j < len(nums):
                nums[i] = nums[j]
                nums[j] = None 
                j += 1
            i += 1
        #print(nums)
        length = 0
        for i in nums:
            if i is not None:
                length += 1
            else:
                break
        return length


