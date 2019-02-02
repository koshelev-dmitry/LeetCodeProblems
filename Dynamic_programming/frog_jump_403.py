class Solution:
    def canCross(self, stones):
        # check the last stone:
        if (len(stones) - 1 > stones[-1] 
                or stones[-1] > (len(stones) - 1)*(len(stones))/2):
            return False
        
        last_stone = stones[-1]
        stones = set(stones)
        jumps_stack = [(1, 1)] # we are at the second stone with k = 1
        while jumps_stack:
            current_stone = jumps_stack.pop()
            pos = current_stone[0]
            k = current_stone[1]
            for dk in [-1,0,1]:
                candidate_stone = pos + k + dk
                if candidate_stone in stones:
                    if pos + k + dk == last_stone:
                        return True
                    if k + dk > 0: 
                        jumps_stack.append((candidate_stone, k + dk))
        return False

        print('while is over')
        return False

print(Solution().canCross([0,1,3,5,6,8,12,17]))