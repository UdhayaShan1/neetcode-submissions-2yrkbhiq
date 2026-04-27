class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        arr = []
        for i in range(n):
            arr.append([])
            for j in range(n):
                arr[i].append(".")
        
        def printer(arr):
            for i in arr:
                print(i)
        
        def validPos(i, j, arr):
            tmp_i = i
            tmp_j = j
            count = 0
            while tmp_i >= 0 and tmp_i < n and tmp_j >= 0 and tmp_j < n:
                if arr[tmp_i][tmp_j] == 'Q':
                    count += 1
                tmp_i -= 1
                tmp_j -= 1
            
            if count >= 2:
                return False

            tmp_i = i
            tmp_j = j
            count = 0
            while tmp_i >= 0 and tmp_i < n and tmp_j >= 0 and tmp_j < n:
                if arr[tmp_i][tmp_j] == 'Q':
                    count += 1
                tmp_i += 1
                tmp_j += 1
            
            if count >= 2:
                return False

            tmp_i = i
            tmp_j = j
            count = 0
            while tmp_i >= 0 and tmp_i < n and tmp_j >= 0 and tmp_j < n:
                if arr[tmp_i][tmp_j] == 'Q':
                    count += 1
                tmp_i -= 1
                tmp_j += 1
            
            if count >= 2:
                return False


            tmp_i = i
            tmp_j = j
            count = 0
            while tmp_i >= 0 and tmp_i < n and tmp_j >= 0 and tmp_j < n:
                if arr[tmp_i][tmp_j] == 'Q':
                    count += 1
                tmp_i += 1
                tmp_j -= 1
            
            if count >= 2:
                return False

            tmp_i = i
            tmp_j = j
            count = 0
            while tmp_i >= 0 and tmp_i < n and tmp_j >= 0 and tmp_j < n:
                if arr[tmp_i][tmp_j] == 'Q':
                    count += 1
                tmp_i -= 1
            
            if count >= 2:
                return False

            tmp_i = i
            tmp_j = j
            count = 0
            while tmp_i >= 0 and tmp_i < n and tmp_j >= 0 and tmp_j < n:
                if arr[tmp_i][tmp_j] == 'Q':
                    count += 1
                tmp_i += 1
            
            if count >= 2:
                return False

            tmp_i = i
            tmp_j = j
            count = 0
            while tmp_i >= 0 and tmp_i < n and tmp_j >= 0 and tmp_j < n:
                if arr[tmp_i][tmp_j] == 'Q':
                    count += 1
                tmp_j -= 1
            
            if count >= 2:
                return False

            tmp_i = i
            tmp_j = j
            count = 0
            while tmp_i >= 0 and tmp_i < n and tmp_j >= 0 and tmp_j < n:
                if arr[tmp_i][tmp_j] == 'Q':
                    count += 1
                tmp_j += 1
            
            if count >= 2:
                return False
            
            return True
        # arr[0][0] = 'Q'
        # arr[1][1] = 'Q'
        # print(validPos(0, 0, arr))
        res = []
        def dfs(row, arr):
            #print(row, arr, '@')
            if row >= n:
                final = []
                for i in arr:
                    final.append(''.join(i))
                res.append([row[:] for row in final])
                return True
            
            for col in range(n):
                arr[row][col] = 'Q'
                if not validPos(row, col, arr):
                    arr[row][col] = '.'
                    continue
                dfs(row+1, arr)
                arr[row][col] = '.'
        dfs(0, arr)

        # for i in res:
        #     printer(i)
        #     print('###########')

        return res
                
            

        