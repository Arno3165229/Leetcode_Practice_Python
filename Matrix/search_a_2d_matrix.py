class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])

        up = 0
        down = m - 1

        while up <= down:
            mid = (up + down) // 2
            if matrix[mid][0] <= target <= matrix[mid][-1]:
                break
            elif target > matrix[mid][-1]:
                up = mid + 1
            else:
                down = mid - 1

        left = 0
        right = n - 1
        row = mid 

        while left <= right:
            mid = (left + right) // 2
            if matrix[row][mid] == target:
                return True
            elif target > matrix[row][mid]:
                left = mid + 1
            else:
                right = mid - 1
        
        return False