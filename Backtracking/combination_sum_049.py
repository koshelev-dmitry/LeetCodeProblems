class Solution:
    def combinationSum(self, candidates: 'List[int]', target: 'int') -> 'List[List[int]]':       
        def dfs_helper(stack, left_to_target):
            if left_to_target == 0:
                res.append(stack)
                return
            for candidate in candidates:
                if candidate > left_to_target: 
                    break
                if not stack or candidate >= stack[-1]: 
                    dfs_helper(stack + [candidate], left_to_target - candidate)
        
        candidates = sorted(candidates)
        res = []
        dfs_helper([], target)

        return res

print(Solution().combinationSum([2,2,3,6,7], 7))