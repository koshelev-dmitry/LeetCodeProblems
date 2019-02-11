'''
Given an unsorted array of integers, find the length of longest increasing subsequence.
Example:
Input: [10,9,2,5,3,7,101,18]
Output: 4 
Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4. 
Note:

There may be more than one LIS combination, it is only necessary for you to return the length.
Your algorithm should run in O(n2) complexity.
Follow up: Could you improve it to O(n log n) time complexity?
'''

class Solution:
    def lengthOfLIS(self, nums):
        if nums == []:
            return 0
        # brute forse:
        # from each element in nums go right to calc how many
        max_subs = [1]*len(nums)
        # 10,9,2,5,3,4
        #  1 1 1 1 1 1
        #  1 1 3 1 2 1
        
        # O(n^2) solution
        # O(n) in space
        # we move from right to left
        for i, num in enumerate(reversed(nums)):
            current_max = 0  # length of longest subsequence
            for j in range(len(nums)-1-i, len(nums)):
                if nums[~i] < nums[j]:
                    current_max = max(current_max, max_subs[j])
            max_subs[~i] += current_max
        return max(max_subs)