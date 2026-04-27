class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        suffixMax = [-float('inf')]
        for i in range(len(prices)-2, -1, -1):
            suffixMax.append(max(prices[i+1], suffixMax[-1]))
        suffixMax = suffixMax[::-1]
        print(suffixMax)

        res = -float('inf')
        for i in range(len(prices)):
            res = max(res, suffixMax[i]-prices[i])
        return max(res, 0)
        