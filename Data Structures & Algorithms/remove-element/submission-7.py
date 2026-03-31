class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0
        for i in range(len(nums)):
            if nums[i] == val:
                continue
            nums[k], nums[i] = nums[i], nums[k]
            k += 1
        count = 0
        for i in range(len(nums)):
            if nums[i] == val:
                break
            count += 1
        return count
