class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        from queue import Queue
        q = Queue()
        dist = {}

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0:
                    q.put((i, j))
                    dist[(i, j)] = 0
        
        while not q.empty():
            curr = q.get()
            for i in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                new_i = curr[0]+i[0]
                new_j = curr[1]+i[1]
                if (new_i, new_j) not in dist:
                    dist[(new_i, new_j)] = float('inf')
                if new_i < 0 or new_j < 0 or new_i >= len(grid) or new_j >= len(grid[0]) or 1+dist[curr] >= dist[(new_i, new_j)] or grid[new_i][new_j] == -1 or grid[new_i][new_j] == 0:
                    continue
                grid[new_i][new_j] = 1+dist[curr]
                dist[(new_i, new_j)] = 1+dist[curr]
                q.put((new_i, new_j))


        