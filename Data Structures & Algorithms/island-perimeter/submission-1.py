class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        
        def explore(r, c):
            
            if (r, c) in visited:
                return 0
            if (r not in range(rows) or c not in range(cols)):
                return 1
            if grid[r][c] == 0:
                return 1
            visited.add((r, c))
            perimeter = 0
            
            directions = [[-1, 0], [1, 0], [0, 1], [0, -1]]

            for dr, dc in directions:
                row, col = r + dr, c + dc
                perimeter += explore(row, col)
            return perimeter
        
        
        rows = len(grid)
        cols = len(grid[0])
        visited = set()
        for r in range(rows):
            for c in range(cols):
                if (r, c) not in visited and grid[r][c] == 1:
                    perimeter = explore(r, c)
        
        return perimeter