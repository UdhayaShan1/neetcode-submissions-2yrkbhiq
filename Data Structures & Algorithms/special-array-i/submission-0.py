class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        even = True if nums[0] % 2 == 0 else False
        for i in range(1, len(nums)):
            curr = True if nums[i] % 2 == 0 else False
            if even == curr:
                return False
            even = curr
        return True
        