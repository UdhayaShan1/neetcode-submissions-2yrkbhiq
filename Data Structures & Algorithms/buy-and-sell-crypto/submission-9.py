class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        s = [-float('inf')]
        for i in range(len(prices)-2, -1, -1):
            s.append(max(s[-1], prices[i+1]))
        s = s[::-1]
        res = 0
        for i in range(len(prices)):
            res = max(res, s[i]-prices[i])
        return res