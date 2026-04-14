class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        adjList = {}
        for i in range(len(isConnected)):
            if i not in adjList:
                adjList[i] = []
            ref = isConnected[i]
            for j in range(len(ref)):
                if ref[j] == 0:
                    continue
                if j not in adjList:
                    adjList[j] = []
                adjList[i].append(j)
                adjList[j].append(i)
        #print(adjList)
        vis = {}
        def dfs(i):
            vis[i] = True
            for n in adjList[i]:
                if n in vis:
                    continue
                dfs(n)
        res = 0
        for i in range(len(isConnected)):
            if i in vis:
                continue
            dfs(i)
            res += 1
        return res

