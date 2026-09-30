from collections import deque

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        def explore(r, c):
            visited.add((r, c))
            directions = [[-1, 0], [0, -1], [1, 0], [0, 1]]
            for dr, dc in directions:
                row, col = r + dr, c + dc
                if (row in range(rows) and col in range(cols) and (row, col) not in visited and grid[row][col] == '1'):
                    visited.add((row, col))
                    explore(row, col)
        
        count = 0
        visited = set()
        rows = len(grid)
        cols = len(grid[0])

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1' and (r, c) not in visited:
                    explore(r, c)
                    count += 1
        
        return count