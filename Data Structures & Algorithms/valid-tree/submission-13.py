class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adjList = {}
        for i in range(n):
            adjList[i] = []
        for i in edges:
            adjList[i[0]].append(i[1])
            adjList[i[1]].append(i[0])
        vis = {}
        def dfs(n, prev):

            vis[n] = True
            for i in adjList[n]:
                if i == prev:
                    continue
                if i in vis:
                    return False
                if not dfs(i, n):
                    return False
            return True
        dfs(0, -1)

        return len(edges) == n-1 and len(vis) == n
