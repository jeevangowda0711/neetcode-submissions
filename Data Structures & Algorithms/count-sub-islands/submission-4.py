class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        ROWS = len(grid1)
        COLS = len(grid1[0])
        visited = set()
        stack = []
        count = 0
        for r in range(ROWS):
            for c in range(COLS):
                if grid2[r][c] == 1 and (r, c) not in visited:
                    stack.append((r, c))

                    res = True
                    while stack:
                        row, col = stack.pop()
                        if (row not in range(ROWS) or col not in range(COLS) or (row, col) in visited or grid2[row][col] == 0):
                            continue
                        visited.add((row,col))

                        if grid1[row][col] == 0:
                            res = False
                        stack.append((row + 1, col))
                        stack.append((row - 1, col))
                        stack.append((row, col + 1))
                        stack.append((row, col - 1))
                    
                    if res:
                        count += 1

        return count