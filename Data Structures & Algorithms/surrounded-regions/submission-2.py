class Solution:
    def solve(self, board: List[List[str]]) -> None:
        vis = {}
        def dfs(i, j, c):
            #print(i, j, c)
            vis[(i, j)] = True
            board[i][j] = c
            for k in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                new_i = i+k[0]
                new_j = j+k[1]
                if new_i < 0 or new_i >= len(board) or new_j < 0 or new_j >= len(board[0]):
                    continue
                if (new_i, new_j) in vis or board[new_i][new_j] != 'O':
                    continue
                dfs(new_i, new_j, c)
        for i in range(len(board)):
            for j in range(len(board[0])):
                if i == 0 or i == len(board)-1 or j == 0 or j == len(board[0])-1:
                    if board[i][j] == 'O':
                        dfs(i, j, 'P')
        #print(board)

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                elif board[i][j] == 'P':
                    board[i][j] = 'O'
        #return board
