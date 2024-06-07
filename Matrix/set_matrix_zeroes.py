class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        row = len(matrix)
        column = len(matrix[0])
        first_row = 1

        for r in range(row):
            for c in range(column):
                if r == 0:
                    if matrix[r][c] == 0:
                        first_row = 0
                        matrix[0][c] = 0
                else:
                    if matrix[r][c] == 0:
                        matrix[r][0] = 0
                        matrix[0][c] = 0
        
        for r in range(1, row):
            for c in range(1, column):
                if matrix[r][0] == 0 or matrix[0][c] == 0:
                    matrix[r][c] = 0
            
        for r in range(row):
            if matrix[0][0] == 0:
                matrix[r][0] = 0
        
        for c in range(column):
            if first_row == 0:
                matrix[0][c] = 0
        
        return matrix
                