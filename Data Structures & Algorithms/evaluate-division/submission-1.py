class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        adjList = {}
        for i in range(len(equations)):
            ref = equations[i]
            if ref[0] not in adjList:
                adjList[ref[0]] = []
            if ref[1] not in adjList:
                adjList[ref[1]] = []
            adjList[ref[0]].append((ref[1], values[i]))
            adjList[ref[1]].append((ref[0], 1/values[i]))

        #print(adjList)
        vis = {}
        def dfs(node, prev, target, prod):
            print(node)
            if node == target:
                if node in adjList:
                    return prod
                return -1
            if node not in adjList:
                return -1
            y1 = -1
            vis[node] = 1
            for i in adjList[node]:
                if i[0] == prev or i[0] in vis:
                    continue
                x = dfs(i[0], node, target, prod*i[1])
                if x >= 0:
                    y1 = x
            return y1
        
        res = []
        for i in queries:
            vis = {}
            res.append(dfs(i[0], None, i[1], 1))
        return res
                


