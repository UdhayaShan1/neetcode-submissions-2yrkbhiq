class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0
        j = 0
        while i < len(nums) and j < len(nums):
            #print(i, j, nums)
            if nums[i] != val and nums[i] != -1:
                i += 1
                #count += 1
                j = max(j, i)
            else:
                while (nums[i] == val or nums[i] == -1) and i < len(nums) and j < len(nums):
                    #nums[i] = -1
                    if nums[j] == val or nums[j] == -1:
                        #count += 1
                        j += 1
                    else:
                        nums[i] = nums[j]
                        nums[j] = -1
                        #count += 1
                        i += 1
                        j += 1
        print(nums)
        count = 0         
        for i in nums:
            if i == val or i == -1:
                break
            count += 1
        return count

