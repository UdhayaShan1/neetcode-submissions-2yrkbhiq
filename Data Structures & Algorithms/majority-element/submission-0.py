class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 0
        cand = None
        for i in nums:
            if i == cand:
                count += 1
            elif count == 0:
                count = 1
                cand = i
            else:
                count -= 1

        # chk = 0
        # for i in nums:
        #     if i == cand:
        #         chk += 1
        return cand