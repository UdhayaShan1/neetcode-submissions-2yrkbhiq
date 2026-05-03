class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adjList = {}
        for i in range(n):
            adjList[i] = []
        for i in edges:
            adjList[i[0]].append(i[1])
            adjList[i[1]].append(i[0])
        #print(edges)
        vis = {}
        def cycle(node, prev):
            vis[node] = True
            for i in adjList[node]:
                if i == prev:
                    continue
                if i in vis:
                    return True
                if cycle(i, node):
                    return True
            return False
        
        if cycle(0, -1):
            return False
        #print(vis)
        return len(vis) == n
                
