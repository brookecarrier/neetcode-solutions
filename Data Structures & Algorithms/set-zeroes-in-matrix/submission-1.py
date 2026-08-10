class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        # for each cell if it == 0
            # store its r and c in lists
        # go thru lists and set the matrix as 0s

        zRows = []
        zCols = []

        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                if matrix[r][c] == 0:
                    zRows.append(r)
                    zCols.append(c)

        for r in zRows:
            matrix[r] = [0 for _ in range(len(matrix[0]))]
        
        for c in zCols:
            for r in range(len(matrix)):
                matrix[r][c] = 0
        
        