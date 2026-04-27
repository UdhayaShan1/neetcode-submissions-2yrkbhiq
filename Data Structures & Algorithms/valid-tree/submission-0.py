class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adjList = {}
        for i in range(n):
            adjList[i] = []
        for i in edges:
            adjList[i[0]].append(i[1])
        

        parent = {}
        vis = {}
        def cyclic(node):

            vis[node] = True
            parent[node] = True
            for i in adjList[node]:
                if i not in vis:
                    if i in parent:
                        return True
                elif i in parent:
                    return True
            del parent[node]
        for i in range(n):
            if cyclic(i):
                return False
        return len(edges) == n-1