class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adjList = {}
        for i in range(n):
            adjList[i] = []
        for i in edges:
            adjList[i[0]].append(i[1])
            adjList[i[1]].append(i[0])
        print(adjList)
        vis = {}
        def dfs(node, prev):
            vis[node] = True
            for i in adjList[node]:
                if i == prev:
                    continue
                if i in vis:
                    return True
                if dfs(i, node):
                    return True
            return False
        for i in range(n):
            if i in vis:
                continue
            res = dfs(i, -1)
            if res:
                #print(i)
                return False
        return len(vis) == n and len(edges) == n-1
