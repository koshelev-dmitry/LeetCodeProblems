"""
Given a sorted (in ascending order) integer array nums of n elements 
and a target value, write a function to search target in nums. 
If target exists, then return its index, otherwise return -1.

Example 1:
Input: nums = [-1,0,3,5,9,12], target = 9
Output: 4
Explanation: 9 exists in nums and its index is 4
"""

class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        l = 0
        r = len(nums) - 1
        while l <= r:
            m = (l + r) // 2
            if target > nums[m]:
                l = m + 1
            elif nums[m] == target:
                return m
            else:
                r = m - 1
        return -1