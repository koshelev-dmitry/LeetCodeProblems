"""
Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

Note:

The solution set must not contain duplicate triplets.

"""
class Solution:
    def threeSum(self, nums):
        nums.sort()
        result = []
        
        for i in range(len(nums)-2):
            if i!=0 and nums[i] == nums[i-1]:
                continue
            target = -nums[i]
            l = i + 1
            r = len(nums) - 1
            while l < r:
                if nums[l] + nums[r] == target:
                    result.append([nums[i],nums[l],nums[r]])
                    l += 1
                    while l < r and nums[l]==nums[l-1]:
                        l += 1
                elif nums[l] + nums[r] < target:
                    l += 1
                else:
                    r -= 1
        return result
                