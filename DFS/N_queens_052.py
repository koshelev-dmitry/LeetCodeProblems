class Solution:
    def totalNQueens(self, n):
        def dfs_helper(ocupied_rows, xy_diff, xy_sum):
            y = len(ocupied_rows)
            nonlocal result
            if y == n:
                result += 1
                return None
            for x in range(n):
                if (x not in ocupied_rows 
                        and x-y not in xy_diff 
                        and x+y not in xy_sum):
                    dfs_helper(ocupied_rows + [x], xy_diff + [x-y], xy_sum + [x+y])
        
        # We start with all empty
        result = 0
        dfs_helper([],[],[])
        return result
