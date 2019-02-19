"""
Solution using dfs not effective
Timelimit execeed
"""
# class Solution:
#     def minPathSum(self, grid: 'List[List[int]]') -> 'int':
#         def helper_dfs(row, col, current_sum):
#             if row > rows:
#                 return float("Inf")
#             if col > cols:
#                 return float("Inf")
            
#             if row == rows and col == cols:
#                 return grid[row][col] + current_sum
            

#             return min(helper_dfs(row+1, col, current_sum + grid[row][col]),
#                        helper_dfs(row, col+1, current_sum + grid[row][col]))

            
#         rows = len(grid) - 1
#         cols = len(grid[0]) - 1
#         return helper_dfs(row=0, col=0, current_sum=0)


"""
Dynamic programming solution:
Idea: 
1) scan over matrix row by row
2) update values of each element
   new value is summ of current + min of two neighbours
"""
class Solution:
    def minPathSum(self, grid: 'List[List[int]]') -> 'int':
        def helper_neighboors_min(row, col):
            if col == 0 and row == 0:
                return 0
            
            if col == 0:
                return grid[row - 1][col]
            
            if row == 0:
                return grid[row][col - 1]
            
            return min(grid[row][col - 1], grid[row - 1][col])
                
            
        rows = len(grid)
        cols = len(grid[0])
        for row in range(rows):
            for col in range(cols):
                grid[row][col] += helper_neighboors_min(row, col)
        return grid[-1][-1]