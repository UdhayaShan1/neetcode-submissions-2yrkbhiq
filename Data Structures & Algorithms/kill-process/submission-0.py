class Solution:
    def killProcess(self, pid: List[int], ppid: List[int], kill: int) -> List[int]:
        adjList = {}
        for i in range(len(pid)):
            if ppid[i] not in adjList:
                adjList[ppid[i]] = []
            adjList[ppid[i]].append(pid[i])
        
        res = []
        vis = {}
        def dfs(node):
            res.append(node)
            vis[node] = True
            if node not in adjList:
                return
            for i in adjList[node]:
                if i in vis:
                    continue
                dfs(i)
        dfs(kill)
        return res