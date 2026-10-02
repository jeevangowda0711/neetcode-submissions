class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        def explore(r, c):
            if (r, c) in visited:
                return 0
            visited.add((r, c))
            length = 1

            directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
            for dr, dc in directions:
                row, col = r + dr, c + dc
                if (row in range(rows) and col in range(cols) and (row, col) not in visited and grid[row][col] == 1):
                    length += explore(row, col)
                    # visited.add((row, col))
            return length
        
        rows = len(grid)
        cols = len(grid[0])
        max_length = 0
        visited = set()
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and (r, c) not in visited:
                    max_length = max(max_length, explore(r, c))
        
        return max_length