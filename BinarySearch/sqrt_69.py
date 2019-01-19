"""
Implement int sqrt(int x).

Compute and return the square root of x, where x is guaranteed to be a non-negative integer.

Since the return type is an integer, the decimal digits are truncated and only the integer part of the result is returned.

Example 1:

Input: 4
Output: 2
Example 2:

Input: 8
Output: 2
Explanation: The square root of 8 is 2.82842..., and since 
             the decimal part is truncated, 2 is returned.
"""


class Solution(object):
    # solution using iterative approach
    # sqrt(N) = 2sqrt(N/4)
    # has the same O(log(n))
    def mySqrt(self, x):
        if x < 4:
            return 0 if x == 0 else 1
        res =  2 * self.mySqrt(x//4)
        return res + 1 if (res + 1)**2 <= x else res


    # solution using Binary search
    def mySqrt_BS(self, x):
        l = 0
        r = x
        while l <= r:
            m = (l + r) // 2
            if m**2 > x:
                r = m - 1
            elif m**2 <= x and (m + 1)**2 > x:
                return m
            else:
                l = m + 1


    # solution using math library is trivial
    def _mySqrt_math(self, x):
        """
        :type x: int
        :rtype: int
        """
        import math
        return int(math.floor(math.sqrt(x)))

solution = Solution()
print(solution.mySqrt(15))