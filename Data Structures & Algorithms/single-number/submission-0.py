class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        no = 0
        for i in nums:
            no ^=i
        return no