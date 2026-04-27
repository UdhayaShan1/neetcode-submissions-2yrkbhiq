class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxP = [-float('inf')]
        for i in range(len(prices)-2, -1, -1):
            maxP.append(max(prices[i+1], maxP[-1]))
        maxP = maxP[::-1]
        #print(maxP)
        res = 0
        for i in range(len(prices)):
            res = max(res, maxP[i]-prices[i])

        return res