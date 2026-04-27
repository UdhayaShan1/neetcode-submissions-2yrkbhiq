class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        p = {0 : 1}
        curr = 0
        res = 0
        for i in nums:
            curr += i
            find = curr-k
            res += p.get(find, 0)
            p[curr] = p.get(curr, 0)+1
        return res
