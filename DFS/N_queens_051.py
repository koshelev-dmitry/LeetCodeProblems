class Solution:
    def solveNQueens(self, n: 'int') -> 'List[List[str]]':
        def dfs_helper(ocupied_rows, xy_diff, xy_sum):
            y = len(ocupied_rows)
            if y == n:
                result.append(ocupied_rows)
                return None
            for x in range(n):
                if (x not in ocupied_rows 
                        and x-y not in xy_diff 
                        and x+y not in xy_sum):
                    dfs_helper(ocupied_rows + [x], xy_diff + [x-y], xy_sum + [x+y])
        
        # We start with all empty
        result = []
        dfs_helper([],[],[])
        return [['.'*x + 'Q' + '.'*(n-x-1) for x in res] for res in result]