class Solution:
    def minimumSemesters(self, n: int, relations: List[List[int]]) -> int:
        adjList = {}
        indeg = {}
        for i in range(n):
            adjList[i+1] = []
            indeg[i+1] = 0
        for i in relations:
            adjList[i[0]].append(i[1])
            indeg[i[1]] += 1


        from queue import deque
        q = deque()
        for i in indeg:
            if indeg[i] == 0:
                q.append(i)
        vis = {}
        while q:
            curr = q.popleft()
            vis[curr] = True
            for i in adjList[curr]:
                indeg[i] -= 1
                if indeg[i] == 0:
                    q.append(i)
        if len(vis) != n:
            return -1
        



        dp = {}
        def dfs(node):
            if len(adjList[node]) == 0:
                return 0
            if node in dp:
                return dp[node]
            res = -1
            for i in adjList[node]:
                res = max(res, dfs(i)+1)
            dp[node] = res
            return res
        
        res = -1
        for i in range(1, n+1):
            res = max(res, dfs(i))
        return res+1

            
