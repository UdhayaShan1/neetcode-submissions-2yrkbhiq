class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        suffix = [-float('inf')]
        for i in range(len(prices)-2, -1, -1):
            suffix.append(max(prices[i+1], suffix[-1]))
        suffix = suffix[::-1]

        #print(suffix)

        res = 0
        for i in range(len(prices)):
            res = max(res, suffix[i]-prices[i])
        return res