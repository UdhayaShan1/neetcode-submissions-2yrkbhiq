class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        start = 0
        end = len(matrix)-1
        ref = []
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if j == 0:
                    ref.append(matrix[i][j])
        
        posRow = -1
        print(ref)
        while start <= end:
            #print(start, end)
            mid = (start+end)//2
            if ref[mid] > target:
                end = mid-1
            else:
                posRow = max(posRow, mid)
                start = mid+1
        #print(posRow)
        if posRow == -1:
            return False
        ref = matrix[posRow]
        start = 0
        end = len(ref)-1
        while start <= end:
            mid = (start+end)//2
            if ref[mid] == target:
                return True
            if target > ref[mid]:
                start = mid+1
            else:
                end = mid-1
        return False