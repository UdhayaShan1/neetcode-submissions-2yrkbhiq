class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            
            ref = i
            while nums[ref] >= 1 and nums[ref] <= len(nums):
                #print(nums)
                shld = nums[ref]-1
                if shld == i:
                    break
                tmp = nums[ref]
                if tmp == nums[shld]:
                    break
                nums[ref] = nums[shld]
                nums[shld] = tmp
        #print(nums)
        chk = 1
        for i in range(len(nums)):
            if nums[i] != chk:
                return chk
            chk += 1
        return chk
        



