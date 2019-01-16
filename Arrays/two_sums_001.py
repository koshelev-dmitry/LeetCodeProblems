class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        cashed_values = {}
        for i in range(len(nums)):
            if nums[i] in cashed_values:
                return [cashed_values[nums[i]],i]
            cashed_values[target - nums[i]] = i
            
            
        return None

solution = Solution()
nums = [2, 7, 11, 15]
target = 13
print(solution.twoSum(nums, target))

