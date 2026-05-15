class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adjList = {}
        for i in range(n):
            adjList[i] = []
        for i in flights:
            adjList[i[0]].append((i[1], i[2]))
        from functools import cache
        @cache
        def dfs(node, k):
            if node == dst:
                return 0
            if k < 0:
                return float('inf')
            res = float('inf')
            for i in adjList.get(node, []):
                res = min(res, dfs(i[0], k-1)+i[1])
            return res
        res = dfs(src, k)
        return res if res != float('inf') else -1