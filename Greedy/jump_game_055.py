class Solution:
    def canJump(self, nums: 'List[int]') -> 'bool':
        max_index = 0
        for i, num in enumerate(nums):
            if i > max_index:
                return False
            max_index = max(num + i, max_index)
            if max_index >= len(nums):
                return True
        return True