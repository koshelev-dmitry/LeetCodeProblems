"""
Write an efficient algorithm that searches for a value 
in an m x n matrix. This matrix has the following properties:

Integers in each row are sorted in ascending from left to right.
Integers in each column are sorted in ascending from top to bottom.
"""

class Solution(object):
    # Using binary search:
    def searchMatrix(self, matrix, target):
        if matrix == [] or matrix ==[[]]:
            return False
        row = 0
        col = len(matrix[0]) - 1        
        while row < len(matrix) and col >= 0:
            if matrix[row][col] == target:
                return True
            elif matrix[row][col] > target:
                col -= 1
            else: 
                row += 1
        return False


A = [[1,   4,  7, 11, 15],
      [2,   5,  8, 12, 19],
      [3,   6,  9, 16, 22],
      [10, 13, 14, 17, 24],
      [18, 21, 23, 26, 30]]    
solution = Solution()
for row in A:
    for element in row:
        print(solution.searchMatrix(A, element)) 
    
        
        
        
        
        
        
        
        
        
        