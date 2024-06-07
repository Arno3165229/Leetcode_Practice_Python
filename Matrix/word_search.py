class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        visited = set()

        for r in range(len(board)):
            for c in range(len(board[0])):
                if self.dfs(r, c, board, word, 0, visited):
                    return True
    
        return False

    def dfs(self, row, column, matrix, word, word_index, visited):
        if row < 0 or row >= len(matrix) or column < 0 or column >= len(matrix[0]) or (row, column) in visited:
            return False
        
        if matrix[row][column] != word[word_index]:
            return False
        
        if word_index == len(word) - 1:
            return True
        
        visited.add((row, column))
        ## DO NOT FORGET to add if under recursive part!!
        if self.dfs(row + 1, column, matrix, word, word_index + 1, visited): return True
        if self.dfs(row, column + 1, matrix, word, word_index + 1, visited): return True
        if self.dfs(row - 1, column, matrix, word, word_index + 1, visited): return True
        if self.dfs(row, column - 1, matrix, word, word_index + 1, visited): return True
        visited.remove((row, column))
        