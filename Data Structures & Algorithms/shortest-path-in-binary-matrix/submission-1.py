class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0] == 1:
            return -1
        directions = [
            (0, 1),   # Right
            (0, -1),  # Left
            (1, 0),   # Down
            (-1, 0),  # Up
            (1, 1),   # Down-Right
            (1, -1),  # Down-Left
            (-1, 1),  # Up-Right
            (-1, -1)  # Up-Left
        ]

        q = deque()
        d = {(0,0): 0}
        q.append((0, 0))
        while q:
            curr = q.popleft()
            for dr, dc in directions:
                new_i = curr[0]+dr
                new_j = curr[1]+dc
                if new_i < 0 or new_j < 0 or new_i >= len(grid) or new_j >= len(grid[0]) or grid[new_i][new_j] == 1 or (new_i, new_j) in d:
                    continue
                d[(new_i, new_j)] = 1+d[curr]
                q.append((new_i, new_j))
        #print(d)

        return d.get((len(grid)-1, len(grid[0])-1), -2)+1
                
