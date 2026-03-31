class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        c1 = None
        count1 = 0
        for i in nums:
            if i == c1:
                count1 += 1
            elif count1 == 0:
                c1 = i
                count1 = 1
            else:
                count1 -= 1
        return c1