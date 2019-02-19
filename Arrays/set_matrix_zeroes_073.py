class Solution:
    def setZeroes(self, matrix: 'List[List[int]]') -> 'None':
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows = len(matrix)
        columns = len(matrix[0])
        row = 0
        column = 0
        for row in range(rows):
            for col in range(columns):
                if matrix[row][col] == 0:
                    
                    # paint rows
                    for i in range(rows):
                        if matrix[i][col] != 0:
                            matrix[i][col] = None
                    
                    # paint columns
                    for i in range(columns):
                        if matrix[row][i] != 0:
                            matrix[row][i] = None
                            
        for row in range(rows):
            for col in range(columns):
                if matrix[row][col] == None:
                    matrix[row][col] = 0
                            
        