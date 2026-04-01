class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        post = [-float('inf')]
        for i in range(len(prices)-2, -1, -1):
            post.append(max(prices[i+1], post[-1]))
        post = post[::-1]
        print(post)
        res = 0
        for i in range(len(prices)):
            res = max(res, post[i]-prices[i])
        return res