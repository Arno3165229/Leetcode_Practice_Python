class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pacific_set = set()
        atlantic_set = set()

        row = len(heights)
        column = len(heights[0])

        def dfs(m, n, visited, prev_height):
            if m < 0 or n < 0 or m >= row or n >= column or (m, n) in visited or heights[m][n] < prev_height: 
                return
            visited.add((m, n)) ## notation for (r, c)
            dfs(m+1, n, visited, heights[m][n])
            dfs(m-1, n, visited, heights[m][n])
            dfs(m, n+1, visited, heights[m][n])
            dfs(m, n-1, visited, heights[m][n])

        for r in range(row):
            dfs(r, 0, pacific_set, heights[r][0])
            dfs(r, column-1, atlantic_set, heights[r][column-1])

        for c in range(column):
            dfs(0, c, pacific_set, heights[0][c])
            dfs(row-1, c, atlantic_set, heights[row-1][c])
        
        result = []

        for r in range(row):
            for c in range(column):
                if (r, c) in pacific_set and (r, c) in atlantic_set: ## notation for (r, c)
                    result.append([r, c]) ## notation for [r, c]

        return result