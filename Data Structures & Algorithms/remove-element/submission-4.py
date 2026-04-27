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
                j = max(j, i)
                continue
            while j < len(nums):
                if nums[j] is None:
                    j += 1
                else:
                    nums[i] = nums[j]
                    nums[j] = None
                    j += 1
                    break
            i += 1
        #print(nums)
        cnt = 0
        for i in nums:
            if i is not None:
                cnt += 1
            else:
                break
        return cnt
            
            