"""
Given a non-empty array of digits representing a non-negative integer, plus one to the integer.

The digits are stored such that the most significant digit is at the head of the list, and each element in the array contain a single digit.

You may assume the integer does not contain any leading zero, except the number 0 itself.
"""

class Solution:
    def plusOne(self, digits: 'List[int]') -> 'List[int]':
        result = []
        keep_in_mind = 1
        for i in range(len(digits)):
            digits[~i] += keep_in_mind
            if digits[~i] > 9:
                digits[~i] %= 10
                keep_in_mind = 1
            else:
                keep_in_mind = 0
        if keep_in_mind == 1:
            return [1] + digits
        else:
            return digits