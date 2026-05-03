class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        d = {0 : 1}
        curr = 0
        res = 0
        for i in nums:
            curr += i
            find = curr-k
            res += d.get(find, 0)
            d[curr] = d.get(curr, 0)+1
        return res
