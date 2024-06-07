class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        left = 0
        right = len(matrix) - 1

        while left < right:
            ## remember
            top = left
            down = right
            for i in range(right - left): ## be careful here
                left_up_tmp = matrix[top][left + i]
                matrix[top][left + i] = matrix[down - i][left]
                matrix[down - i][left] = matrix[down][right - i]
                matrix[down][right - i] = matrix[top + i][right]
                matrix[top + i][right] = left_up_tmp
            
            left += 1
            right -= 1
        
        return matrix