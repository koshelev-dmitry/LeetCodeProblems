class Solution:
    def uniquePaths(self, m, n):
        # def factorial(k, count):
        #     if k == 0:
        #         return 1
        #     res = 1
            
        #     for i in range(count):
        #         res *= k-i
        #     return res
        
        # if m > n:
        #     n, m = m, n
        # if m == 0 or n == 0:
        #     return 0
        # return int(factorial(n + m - 2, m - 1) / factorial(m - 1, m - 1))

        # code refactoring
        if m == 0 or n == 0:
            return 0
        # m should be not greater that n 
        if m > n:
            n, m = m, n
        
        numerator = 1
        denumerator = 1
        for i in range(m-1):
            numerator *= (n - 1 + m - 1 - i)
            denumerator *= (m - 1 - i)
        return int(numerator / denumerator)


print(Solution().uniquePaths(57,2))