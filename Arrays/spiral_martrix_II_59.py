class Solution:
    def generateMatrix(self, n):
        result = [[0 for i in range(n)] for j in range(n)] # empty matrix
        count = 1
        left = 0
        right = n-1
        top = 0
        bottom = n-1
        while left <= right and top <= bottom:
            # right
            for i in range(left, right + 1):
                result[top][i] = count
                count += 1
            top += 1
            
            # down
            for i in range(top, bottom + 1):
                result[i][right] = count
                count += 1
            right -= 1
            
            if left < right and top < bottom:
                # left
                for i in reversed(range(left, right + 1)):
                    result[bottom][i] = count
                    count += 1
                bottom -= 1

                # up
                for i in reversed(range(top, bottom + 1)):
                    result[i][left] = count
                    count += 1
                left += 1
        return result
