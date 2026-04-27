class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        chk = {}
        for i in nums:
            if i in chk:
                return True
            chk[i] = True
        return False