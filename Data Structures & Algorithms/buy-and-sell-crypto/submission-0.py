class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        prefix_r = [-float('inf')]
        for i in range(len(prices)-2, -1, -1):
            prefix_r.append(max(prices[i+1], prefix_r[-1]))
        prefix_r = prefix_r[::-1]
        #print(prefix_r)
        res = 0
        for i in range(len(prices)):
            res = max(res, prefix_r[i]-prices[i])
        return res
