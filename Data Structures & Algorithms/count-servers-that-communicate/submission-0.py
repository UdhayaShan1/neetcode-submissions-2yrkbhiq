class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        r = {}
        c = {}
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 1:
                    r[row] = r.get(row, 0)+1
                    c[col] = c.get(col, 0)+1
        print(r, c)


        res = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 1:
                    if r[row] > 1 or c[col] > 1:
                        res += 1
        return res