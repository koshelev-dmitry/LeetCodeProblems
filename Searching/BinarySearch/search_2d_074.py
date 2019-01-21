"""
Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

Integers in each row are sorted from left to right.
The first integer of each row is greater than the last integer of the previous row.
Example 1:

Input:
matrix = [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
target = 3
Output: true
Example 2:

Input:
matrix = [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
target = 13
Output: false
"""

class Solution(object):
    def searchMatrix(self, matrix, target):
        def binary_search(column, target):
            l = 0
            r = len(column) - 1
            while l<=r:
                m = (l + r) // 2
                if m == len(column)-1:
                    return m
                if column[m] <= target < column[m+1] :
                    return m
                elif column[m] > target:
                    r = m - 1
                else:
                    l = m + 1
            return m
        
        if matrix == [] or matrix == [[]]:
            return False
        if target < matrix[0][0] or matrix[-1][-1] < target:
            print("Element lies out of the range")
            return False
        
        column = []
        for i in range(len(matrix)):
            column.append(matrix[i][0])

        row_index = binary_search(column, target)
        row = matrix[row_index]
        position = binary_search(row, target)
        if row[position] != target:
            print(f'Element={target} is not in the row={row}')
            return False

        return True


matrix = [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [21, 22, 23, 24],
  [23, 30, 34, 50]
]
solution = Solution()
print(solution.searchMatrix(matrix, 2))