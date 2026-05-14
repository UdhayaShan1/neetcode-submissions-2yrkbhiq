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

        def bfs(s, dst):
            if s not in adjList:
                return -1
            q = deque()
            q.append(s)
            d = {s: 1}
            while q:
                curr = q.popleft()
                for i in adjList.get(curr, []):
                    if i[0] in d:
                        continue
                    d[i[0]] = i[1]*d[curr]
                    q.append(i[0])
            return d.get(dst, -1)
        res = []
        for i in queries:
            res.append(bfs(i[0], i[1]))
        return res