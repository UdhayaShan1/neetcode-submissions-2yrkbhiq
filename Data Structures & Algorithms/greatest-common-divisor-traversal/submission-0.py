class Solution:
    def canTraverseAllPairs(self, nums: List[int]) -> bool:
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
        dsu = DSU(len(nums))

        index = {}
        for i in range(len(nums)):
            ref = nums[i]
            if ref == 1:
                return False
            for k in range(2, int(ref**0.5)+1):

                while ref % k == 0:
                    if k not in index:
                        index[k] = i
                    else:
                        dsu.union(i, index[k])
                    ref //= k
                if ref < k:
                    break
            if ref > 1:
                if ref not in index:
                    index[ref] = i
                else:
                    dsu.union(i, index[ref])
        return dsu.Size[dsu.find(0)] == len(nums)

        # return True
                
