class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        chk = {}
        chk[0] = 1
        res = 0
        curr = 0
        for i in nums:
            curr += i
            find = curr-goal
            #print(curr, find, chk)
            res += chk.get(find, 0)
            chk[curr] = chk.get(curr, 0)+1
        return res