class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
                
        self.rows = len(grid)
        self.cols = len(grid[0])
        visited = set()
        for r in range(self.rows):
            for c in range(self.cols):
                if (r, c) not in visited and grid[r][c] == 1:
                    perimeter = self.explore(r, c, visited, grid)
        
        return perimeter


    def explore(self, r, c, visited, grid):
            
        if (r, c) in visited:
            return 0
        if (r not in range(self.rows) or c not in range(self.cols)):
            return 1
        if grid[r][c] == 0:
            return 1
        visited.add((r, c))
        perimeter = 0
        
        directions = [[-1, 0], [1, 0], [0, 1], [0, -1]]

        for dr, dc in directions:
            row, col = r + dr, c + dc
            perimeter += self.explore(row, col, visited, grid)
        return perimeter