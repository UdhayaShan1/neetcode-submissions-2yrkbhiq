class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        for i in range(len(matrix)):
            for j in range(i+1, len(matrix[0])):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        
        i = 0
        j = len(matrix[0])-1
        while i < j:
            for k in range(len(matrix)):
                matrix[k][i], matrix[k][j] = matrix[k][j], matrix[k][i]
            i += 1
            j -= 1
        