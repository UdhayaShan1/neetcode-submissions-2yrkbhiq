class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        vis = {}
        def dfs(i, j, ref):
            if ref == word:
                return True
            if i < 0 or j < 0 or i >= len(board) or j >= len(board[0]):
                return False
            for k in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
                new_i = i+k[0]
                new_j = j+k[1]
                if (new_i, new_j) in vis:
                    continue
                vis[(i,j)] = 1
                if dfs(new_i, new_j, ref+board[i][j]):
                    return True
                del vis[(i,j)]
            return False
        for i in range(len(board)):
            for j in range(len(board[0])):
                if dfs(i, j, ""):
                    return True
        return False

                