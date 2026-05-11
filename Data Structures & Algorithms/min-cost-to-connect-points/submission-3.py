class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        class DSU:
            def __init__(self, n):
                self.Parent = list(range(n + 1))
                self.Size = [1] * (n + 1)

            def find(self, node):
                if self.Parent[node] != node:
                    self.Parent[node] = self.find(self.Parent[node])
                return self.Parent[node]

            def union(self, u, v):
                pu = self.find(u)
                pv = self.find(v)
                if pu == pv:
                    return False
                if self.Size[pu] < self.Size[pv]:
                    pu, pv = pv, pu
                self.Size[pu] += self.Size[pv]
                self.Parent[pv] = pu
                return True
        ufds = DSU(len(points))
        # for i in range(len(points)):
        #     points[i].append(i)
        edges = []
        for i in range(len(points)):
            for j in range(i+1, len(points)):
                ref = points[i]
                ref1 = points[j]
                d = abs(ref[0]-ref1[0])+abs(ref[1]-ref1[1])
                edges.append([i, j, d])
        edges.sort(key=lambda x:x[2])

        c = 0
        res = 0
        for i in edges:
            if ufds.union(i[0], i[1]):
                c += 1
                res += i[-1]
            if c == len(points)-1:
                return res
        return res




