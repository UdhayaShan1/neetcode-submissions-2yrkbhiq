class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        from functools import cache

        @cache
        def dfs(k1, day):
            if k1 >= len(days):
                return 0
            if days[k1] <= day:
                return dfs(k1+1, day)
            else:
                res = float('inf')
                for i in range(len(costs)):
                    actl = -1
                    if i == 0:
                        actl = 1
                    elif i == 1:
                        actl = 7
                    else:
                        actl = 30
                    res = min(res, dfs(k1+1, days[k1]+actl-1) + costs[i])
                return res
        return dfs(0, -1)
