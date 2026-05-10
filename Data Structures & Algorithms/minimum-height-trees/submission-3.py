class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]
        # return []
        adjList = {}
        indeg = {}
        for i in range(n):
            adjList[i] = []
            indeg[i] = 0
        for i in edges:
            indeg[i[0]] += 1
            indeg[i[1]] += 1
            adjList[i[0]].append(i[1])
            adjList[i[1]].append(i[0])
        q = deque()
        for i in indeg:
            if indeg[i] == 1:
                q.append(i)
        while q:
            if n <= 2:
                return list(q)
            for i in range(len(q)):
                node = q.popleft()
                n -= 1
                for j in adjList[node]:
                    indeg[j] -= 1
                    if indeg[j] == 1:
                        q.append(j)
            