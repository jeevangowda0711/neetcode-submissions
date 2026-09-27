class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []

        while matrix:
            # right, matrix level pop
            res += matrix.pop(0)
            # down, row level pop - last elements
            if matrix and matrix[0]:
                for row in matrix:
                    res.append(row.pop())
            # left, matrix level pop in reverse
            if matrix:
                res += matrix.pop()[::-1]
            # up, row level pop - first elements - reverse ordered matrix
            if matrix and matrix[0]:
                for row in matrix[::-1]:
                    res.append(row.pop(0))
            
        return res