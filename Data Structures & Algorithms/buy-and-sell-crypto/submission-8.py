class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        m = [-float('inf')]
        for i in range(len(prices)-2, -1, -1):
            m.append(max(m[-1], prices[i+1]))
        m = m[::-1]
        res = 0
        for i in range(len(prices)):
            res = max(res, m[i]-prices[i])
        return res