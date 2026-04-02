class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adjList = {}
        for i in range(n):
            adjList[i] = []
        for i in edges:
            adjList[i[0]].append(i[1])
            adjList[i[1]].append(i[0])
        
        vis = {}
        def dfs(node, prev):
            if node in vis:
                return False

            vis[node] = True
            res = True
            for i in adjList[node]:
                if i == prev:
                    continue
                res = res and dfs(i, node)
            return res
        return dfs(0, -1) and len(vis) == n

        