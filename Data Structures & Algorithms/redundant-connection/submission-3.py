class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        indeg = {}
        adjList = {}
        for i in edges:
            indeg[i[0]] = indeg.get(i[0], 0)+1
            indeg[i[1]] = indeg.get(i[1], 0)+1
            if i[0] not in adjList:
                adjList[i[0]] = []
            if i[1] not in adjList:
                adjList[i[1]] = []
            adjList[i[0]].append(i[1])
            adjList[i[1]].append(i[0])
        
        q = deque()
        for i in indeg:
            if indeg[i] == 1:
                q.append(i)
        
        path = {}
        while q:
            curr = q.popleft()
            path[curr] = 1
            for i in adjList[curr]:
                indeg[i] -= 1
                if indeg[i] == 1:
                    q.append(i)
        print(path)

        in_cycle = {}
        for i in edges:
            if i[0] not in path:
                in_cycle[i[0]] = True
            if i[1] not in path:
                in_cycle[i[1]] = True
        print(in_cycle)

        for i in range(len(edges)-1, -1, -1):
            ref = edges[i]
            if ref[0] in in_cycle and ref[1] in in_cycle:
                return ref
            


