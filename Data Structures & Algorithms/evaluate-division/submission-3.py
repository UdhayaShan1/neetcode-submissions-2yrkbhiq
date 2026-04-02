class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        adjList = {}
        pos = {}
        for i in range(len(equations)):
            ref = equations[i]
            pos[ref[0]] = 1
            pos[ref[1]] = 1
            if ref[0] not in adjList:
                adjList[ref[0]] = []
            if ref[1] not in adjList:
                adjList[ref[1]] = []
            adjList[ref[0]].append((ref[1], values[i]))
            adjList[ref[1]].append((ref[0], 1/values[i]))
        print(adjList)

        def q(query):
            if query[0] not in pos or query[1] not in pos:
                return -1
            d = {} 
            from collections import deque
            q = deque()
            q.append(query[0])
            d[query[0]] = 1
            while q:
                curr = q.popleft()
                if curr not in adjList:
                    continue
                for i in adjList[curr]:
                    if i[0] in d:
                        continue
                    d[i[0]] = d[curr]*i[1]
                    q.append(i[0])
            print(d)
            return d.get(query[1], -1)
        res = []
        for i in queries:
            res.append(q(i))
        return res
