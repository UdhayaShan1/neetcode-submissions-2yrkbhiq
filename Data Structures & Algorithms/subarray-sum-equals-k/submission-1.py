class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        chk = {}
        curr = 0
        chk[0] = 1
        res = 0
        for i in nums:
            curr += i
            find = curr-k
            res += chk.get(find, 0)
            chk[curr] = chk.get(curr, 0)+1
        return res



