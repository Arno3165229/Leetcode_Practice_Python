class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        result = []
        self.dfs(0, 0, matrix, False, result)
        return result

    
    def dfs(self, row, column, matrix, upper_flag, spiralorder):
        if row < 0 or row >= len(matrix) or column < 0 or column >= len(matrix[0]) or matrix[row][column] == '#':
            return
        spiralorder.append(matrix[row][column])
        matrix[row][column] = '#'

        if upper_flag == True:
            self.dfs(row - 1, column, matrix, True, spiralorder)

        self.dfs(row, column + 1, matrix, False, spiralorder)
        self.dfs(row + 1, column, matrix, False, spiralorder)
        self.dfs(row, column - 1, matrix, False, spiralorder)
        self.dfs(row - 1, column, matrix, True, spiralorder)