class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        s = 0
        e = len(matrix)-1
        res = float('inf')
        while s <= e:
            mid = (s+e)//2
            if matrix[mid][-1] < target:
                s = mid+1
            else:
                res = mid
                e = mid-1
        if res == float('inf'):
            return False
        row = matrix[res]
        #print(row)
        s = 0
        e = len(row)-1
        while s <= e:
            mid = (s+e)//2
            #print(s, e, mid, row[mid], target)
            if row[mid] == target:
                return True
            if row[mid] < target:
                s = mid+1
            else:
                e = mid-1
        return False