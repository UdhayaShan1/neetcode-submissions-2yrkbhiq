class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        res = []
        for i in range(n):
            res.append([0]*n)
        print(res)
        moves = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        curr_m = 0

        i = 0
        j = 0
        for k in range(1, n**2+1):
            res[i][j] = k

            move = moves[curr_m]
            new_i = i+move[0]
            new_j = j+move[1]
            if new_i < 0 or new_j < 0 or new_i >= n or new_j >= n or res[new_i][new_j] != 0:
                curr_m += 1
                curr_m %= len(moves)
                move = moves[curr_m]
                new_i = i+move[0]
                new_j = j+move[1]
            #print(i, j, new_i, new_j)
            i = new_i
            j = new_j
        return res
            



