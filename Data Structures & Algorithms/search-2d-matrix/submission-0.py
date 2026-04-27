class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def findRow():
            start = 0 
            end = len(matrix)-1
            res = -1
            while start <= end:
                mid = (start+end)//2
                if matrix[mid][-1] < target:
                    start = mid+1
                elif matrix[mid][0] > target:
                    end = mid-1
                else:
                    res = mid
                    break
            return res
        #print(findRow())

        row = matrix[findRow()]
        start = 0
        end = len(row)-1
        while start <= end:
            mid = (start+end)//2
            if row[mid] == target:
                return True
            if row[mid] > target:
                end = mid-1
            else:
                start = mid+1
        return False
