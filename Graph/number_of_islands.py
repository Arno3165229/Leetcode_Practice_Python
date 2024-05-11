class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        row = len(grid)
        column = len(grid[0])

        visited = set()
        count = 0

        def dfs(r, c, visited):
            if r < 0 or c < 0 or r >= row or c >= column or (r, c) in visited or grid[r][c] == '0':
                return
            visited.add((r, c))
            dfs(r+1, c, visited)
            dfs(r-1, c, visited)
            dfs(r, c+1, visited)
            dfs(r, c-1, visited)

        for r in range(row):
            for c in range(column):
                if grid[r][c] == '1': ## be careful, only want '1' go into dfs
                    if (r, c) not in visited: ## be careful, only make (r, c) not in visited go into dfs
                        dfs(r, c, visited)
                        count += 1
        
        return count
