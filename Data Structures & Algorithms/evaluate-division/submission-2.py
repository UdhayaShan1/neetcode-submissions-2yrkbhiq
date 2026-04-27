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
        
        from collections import deque
        res = []
        for i in queries:
            dist = {}
            q = deque()
            q.append(i[0])
            dist[i[0]] = 1
            while q:
                curr = q.popleft()
                if curr not in adjList:
                    continue
                for k in adjList[curr]:
                    t = k[0]
                    v = k[1]
                    if t in dist:
                        continue
                    dist[t] = dist[curr]*v
                    q.append(t)
            print(i, dist)
            if i[1] not in dist or i[0] not in adjList:
                res.append(-1)
            else:
                res.append(dist[i[1]])
        return res


