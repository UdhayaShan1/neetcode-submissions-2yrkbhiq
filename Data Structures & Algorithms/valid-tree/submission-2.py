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
            
            vis[node] = True
            res = True
            for i in adjList[node]:
                if i == prev:
                    continue
                if i in vis:
                    return False
                res = res and dfs(i, node)
            return res
        for i in range(n):
            if i in vis:
                continue
            if not dfs(i, -1):
                return False
        return len(edges) == n-1


