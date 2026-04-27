class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        adjList = {}
        for i in range(1, len(edges)+1):
            adjList[i] = []
        for i in edges:
            adjList[i[0]].append(i[1])
            adjList[i[1]].append(i[0])
        
        vis = {}
        ans = {}
        def dfs(node, prev):
            if node in vis:
                ans2 = [node, prev]
                ans2.sort()
                ans[tuple(ans2)] = 1
                return
            vis[node] = 1
            for i in adjList[node]:
                if i == prev:
                    continue
                dfs(i, node)
        
        for i in range(len(edges), 0, -1):
            vis = {}
            dfs(i, -1)
        #print(ans)
        for i in range(len(edges)-1, -1, -1):
            if tuple(edges[i]) in ans:
                return edges[i]
            
        
        