class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        chk = {}
        def dfs(i, j, str1):
            if str1 == word:
                return True
            if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]):
                return False
            
            for k in [(0, -1), (0, 1), (1, 0), (-1, 0)]:
                new_i = i + k[0]
                new_j = j + k[1]
                if (new_i, new_j) not in chk:
                    chk[(i,j)] = 1
                    if dfs(new_i, new_j, str1+board[i][j]):
                        del chk[(i,j)]
                        return True
                    del chk[(i,j)]
            return False
        
        #print(dfs(0, 2, ""))
        for i in range(len(board)):
            for j in range(len(board[0])):
                if dfs(i, j, ""):
                    return True
        return False
                
                    
