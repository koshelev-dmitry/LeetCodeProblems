"""
Given a 32-bit signed integer, reverse digits of an integer.
Runtime: 28 ms, faster than 100.00% of Python online submissions for Reverse Integer.
"""

class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        sign = 1 if x >=0 else -1
        rev = sign*int(str(abs(x))[::-1])
        if rev <= -1*(2**31) or rev > 2**31:
            return 0 
        else:
            return rev