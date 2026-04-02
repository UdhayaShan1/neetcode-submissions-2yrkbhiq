class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        q = deque()
        d = {}
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 0:
                    q.append((i, j))
                    d[(i, j)] = 0
        
        print(d)
        while q:
            curr = q.popleft()
            for i in [(0, -1), (0, 1), (1, 0), (-1, 0)]:
                new_i = curr[0]+i[0]
                new_j = curr[1]+i[1]
                ref = (new_i, new_j)
                if ref in d:
                    continue
                if new_i < 0 or new_j < 0 or new_i >= len(grid) or new_j >= len(grid[0]) or grid[new_i][new_j] == -1:
                    continue
                d[ref] = 1+d[curr]
                q.append(ref)
        print(d)
        res = []
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                grid[i][j] = d.get((i,j), -1)
