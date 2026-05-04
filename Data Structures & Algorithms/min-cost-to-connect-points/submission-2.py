class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        class DSU:
            def __init__(self, n):
                self.parents = list(range(n+1))
                self.size = [1]*(n+1)
            
            def find(self, node):
                if self.parents[node] != node:
                    self.parents[node] = self.find(self.parents[node])
                return self.parents[node]
            
            def union(self, u, v):
                #print(u, v)
                pu = self.find(u)
                pv = self.find(v)
                if pu == pv:
                    return False
                if self.size[pu] < self.size[pv]:
                    pu, pv = pv, pu
                self.size[pu] += self.size[pv]
                self.parents[pv] = pu
                return True

        dsu = DSU(len(points))    
        edges = []
        for i in range(len(points)):
            for j in range(i+1, len(points)):
                r1 = points[i]
                r2 = points[j]
                edges.append((i, j, abs(r1[0]-r2[0]) + abs(r1[1] - r2[1])))
        edges.sort(key = lambda x : x[2])
        #print(edges)
        cost = 0
        count = 0
        for i in edges:
            if dsu.union(i[0], i[1]):
                cost += i[2]
                count += 1
                if count == len(points)-1:
                    return cost
        return cost


