class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        edges = []
        for i in range(len(points)):
            ref = points[i]
            for j in range(i+1, len(points)):
                ref2 = points[j]
                dist = abs(ref2[0]-ref[0]) + abs(ref2[1]-ref[1])
                edges.append((i, j, dist))
        #print(edges)
        edges.sort(key=lambda x:x[-1])
        #print(edges)

        parent = [i for i in range(len(points))]
        rank = [0] * len(points)

        def find(i):
            if parent[i] == i:
                return i
            # Path Compression
            parent[i] = find(parent[i])
            return parent[i]

        def union(i, j):
            root_i = find(i)
            root_j = find(j)
            if root_i != root_j:
                # Union by Rank
                if rank[root_i] > rank[root_j]:
                    parent[root_j] = root_i
                elif rank[root_i] < rank[root_j]:
                    parent[root_i] = root_j
                else:
                    parent[root_j] = root_i
                    rank[root_i] += 1
                return True
            return False
        res = 0
        for i in edges:
            ref = union(i[0], i[1])
            if not ref:
                continue
            res += i[-1]
        return res
