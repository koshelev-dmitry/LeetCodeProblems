"""
Given an unsorted array of integers, find the length of longest increasing subsequence.

Example:
Input: [10,9,2,5,3,7,101,18]
Output: 4 
Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4. 
"""

class Solution:
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Brute force approach O(n^2)
        if nums == []:
            return 0
        # brute forse:
        # from each element in nums go right to calc how many
        max_subs = [1]*len(nums)
        # 10,9,2,5,3,4
        #  1 1  1 1 1
        for i, num in enumerate(reversed(nums)):
            current_max = 0
            for j in range(len(nums)-1-i, len(nums)):
                if nums[~i] < nums[j]:
                    current_max = max(current_max, max_subs[j])
            max_subs[~i] += current_max
        return max(max_subs)