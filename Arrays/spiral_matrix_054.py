class Solution(object):
    def spiralOrder(self, matrix):
        if matrix == [[]] or matrix == []:
            return []
        rows = len(matrix) - 1
        cols = len(matrix[0]) -1
        
        left = 0
        right = cols
        bottom = rows
        top = 0
        
        result = []
        
        while left<=right and top<=bottom:
            # move right
            for i in range(left, right+1):
                # print(f"move right {matrix[top][i]}")
                result.append(matrix[top][i])
            top += 1
            
            # move down
            for i in range(top, bottom+1):
                # print(f"move down {matrix[i][right]}")
                result.append(matrix[i][right])
            right -= 1
            

            if left<=right and top<=bottom:
                # move left
                for i in reversed(range(left, right+1)):
                    # print(f"move left {matrix[bottom][i]}")
                    result.append(matrix[bottom][i])
                bottom -= 1
                
                # move up
                for i in reversed(range(top, bottom+1)):
                    # print(f"move up {matrix[i][left]}")
                    result.append(matrix[i][left])
                left += 1
            
        return result

matrx = [[1,2,3,4]]
print(Solution().spiralOrder(matrx))