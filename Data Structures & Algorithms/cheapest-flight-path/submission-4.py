class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adjList = {}
        for i in range(n):
            adjList[i] = []
        
        for i in flights:
            adjList[i[0]].append((i[1], i[2]))
        dp = {}
        def dfs(node, stops):
            if node == dst:
                return 0
            if stops < 0:
                return float('inf')
            key = (node, stops)
            if key in dp:
                return dp[key]
            res = float('inf')
            for i in adjList[node]:
                res = min(res, dfs(i[0], stops-1)+i[1])
            dp[key] = res
            return res
        res = dfs(src, k)
        return res if res != float('inf') else -1

