class Solution:
    def leadsToDestination(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        indeg = {}
        outdeg = {}
        adjList = {}
        for i in range(n):
            indeg[i] = 0
            outdeg[i] = 0
            adjList[i] = []
        for i in edges:
            indeg[i[1]] += 1
            outdeg[i[0]] += 1
            adjList[i[0]].append(i[1])
        
        vis = {}
        def dfs(node):
            vis[node] = True
            for i in adjList[node]:
                if i in vis:
                    continue
                dfs(i)
        dfs(source)

        for i in vis:
            if i != destination and outdeg[i] == 0:
                return False
        
        from queue import deque

        q = deque()
        for i in indeg:
            if i in vis and indeg[i] == 0:
                q.append(i)
        hmm = {}
        while q:
            curr = q.popleft()
            hmm[curr] = True
            for i in adjList[curr]:
                indeg[i] -= 1
                if indeg[i] == 0:
                    q.append(i)
        if len(hmm) != len(vis):
            return False


        return True


