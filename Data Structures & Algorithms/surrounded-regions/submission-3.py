class Solution:
    def solve(self, board: List[List[str]]) -> None:
        vis = {}
        def dfs(i, j, c):
            if i < 0 or j < 0 or i >= len(board) or j >= len(board[0]) or (i, j) in vis or board[i][j] == 'X':
                return
            vis[(i, j)] = True
            board[i][j] = c
            dfs(i+1, j, c)
            dfs(i-1, j, c)
            dfs(i, j+1, c)
            dfs(i, j-1, c)
        for i in range(len(board)):
            for j in range(len(board[0])):
                if i == 0 or i == len(board)-1 or j == 0 or j == len(board[0])-1:
                    if board[i][j] == 'O':
                        dfs(i, j, 'P')
        print(board)

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == 'P':
                    board[i][j] = 'O'
                elif board[i][j] == 'O':
                    board[i][j] = 'X'
        
                
                    