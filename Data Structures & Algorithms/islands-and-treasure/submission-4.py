class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        q = deque()
        d = {}
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0:
                    q.append((i, j))
                    d[(i, j)] = 0
        while q:
            curr = q.popleft()
            for k in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                new_i = curr[0]+k[0]
                new_j = curr[1]+k[1]
                if new_i < 0 or new_j < 0 or new_i >= len(grid) or new_j >= len(grid[0]) or (new_i, new_j) in d or grid[new_i][new_j] == -1:
                    continue
                d[(new_i, new_j)] = 1+d[curr]
                q.append((new_i, new_j))
        #print(d)

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                grid[i][j] = d.get((i, j), grid[i][j])
        

            